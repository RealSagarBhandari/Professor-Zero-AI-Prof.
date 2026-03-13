# app.py - web view for my project 2 ML

#
# this is the entrance. I am using streamlit for UI instead of jupyter
# its way easier to share with ppl 

import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# custom settings for my fictional professor Absolute Zero
from src.settings import MODEL_NAME, SYSTEM_PROMPT, PAGE_TITLE, PAGE_ICON, SIDEBAR_QUOTES, PROFESSOR_IMAGE
from src.core_logic import make_start_msgs

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# sidebar stuff showing quotes and image 
with st.sidebar:
    try:
        st.image(PROFESSOR_IMAGE, caption="Professor Absolute Zero", width="stretch")
    except:
        st.write("**Professor Absolute Zero**")
    
    st.markdown("---")
    for q in SIDEBAR_QUOTES:
        st.write(f"**{q}**")
        st.markdown("---")

# main area headers 
st.title("Professor Absolute Zero")
st.caption("Professor of Theoretical Astrophysics | Cosmology & Dark Matter")

# session state helps not lose history when rerunning the script
# very important!! otherwise model gets amnesia every click
if "msgs" not in st.session_state:
    st.session_state.msgs = make_start_msgs()

if "brain" not in st.session_state:
    # connect only once
    st.session_state.brain = ChatOllama(model=MODEL_NAME)

# display old texts skipping system ones
for m in st.session_state.msgs:
    if isinstance(m, HumanMessage):
        with st.chat_message("user"):
            st.markdown(m.content)
    elif isinstance(m, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(m.content)

# where user talks
if user_text := st.chat_input("Ask a question about the cosmos..."):
    # add to visual and list
    st.session_state.msgs.append(HumanMessage(content=user_text))
    with st.chat_message("user"):
        st.markdown(user_text)
    
    # generate streaming response
    with st.chat_message("assistant"):
        ui_holder = st.empty()
        full_text = ""
        
        try:
            for piece in st.session_state.brain.stream(st.session_state.msgs):
                full_text += piece.content
                ui_holder.markdown(full_text + "▌") # blinking cursor thinggy
            
            ui_holder.markdown(full_text)
            
            st.session_state.msgs.append(AIMessage(content=full_text))
            
        except Exception as e:
            st.error(f"broke: {e}")
            st.info("run ollama serve maybe?")
