# core_logic.py - the main brain for chatbot I am working on 

# This file has main stuff for the bot. trying to make it act like Professor Absolute Zero, 
#

# I am using combination here!
#
# A) system prompt (kinda like rag context injection)
# B) conversation history (my own mini RAG where i just send the whole thing lol)

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import sys

from src.settings import MODEL_NAME, SYSTEM_PROMPT

# start ollama connection. simplified vs huggingface models
def init_llm():
    """this starts the ollama client"""
    try:
        llm = ChatOllama(model=MODEL_NAME)
        # test if working
        llm.invoke([SystemMessage(content="test")])
        return llm
    except Exception as e:
        print(f"ollama broke: {e}")
        print("start ollama first (ollama serve)")
        return None

def make_start_msgs():
    """initial setup with prompt"""
    return [SystemMessage(content=SYSTEM_PROMPT)]

def get_answer(llm, msgs, stream=True):
    """
    generates answer. sending ALL old msgs for context so it remembers stuff
    test this later to c how far back it remebers
    """
    if stream:
        return llm.stream(msgs)
    else:
        return llm.invoke(msgs).content

def add_user(msgs, text):
    """putting user msg in list"""
    msgs.append(HumanMessage(content=text))
    return msgs

def add_bot(msgs, text):
    """putting ai response in the list"""
    msgs.append(AIMessage(content=text))
    return msgs

# small term loop just like cell testing
def test_term_chat():
    """cmd line chatting for quick test, may for .. idk"""
    print("=" * 40)
    print("Professor Absolute Zero Bot Terminal Testing")
    print("=" * 40)
    
    llm = init_llm()
    if not llm:
        sys.exit(1)
        
    print("ready. type exit to stop.\n")
    
    hist = make_start_msgs()
    
    while True:
        try:
            inp = input("\nU: ")
            if inp.lower() in ["exit", "quit", "bye"]:
                print("\nProfessor Absolute Zero: Im done too. go read a book.") #no harsh feelings 
                break
                
            hist = add_user(hist, inp)
            
            print("\nProfessor Absolute Zero: ", end="", flush=True)
            text_resp = ""
            
            for chunk in get_answer(llm, hist, stream=True):
                print(chunk.content, end="", flush=True)
                text_resp += chunk.content
                
            print()
            hist = add_bot(hist, text_resp)
            
        except KeyboardInterrupt:
            print("\n\nProfessor Absolute Zero: Class dismissed.")
            break
        except Exception as e:
            print(f"\nerror happened: {e}")

if __name__ == "__main__":
    test_term_chat()
