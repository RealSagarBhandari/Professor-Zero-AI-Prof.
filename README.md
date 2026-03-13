# Professor Absolute Zero: LLM-Powered Conversational Agent 

An interactive chatbot using AI technology that simulates the persona of **Professor Absolute Zero**, a slightly cynical, brilliant, and deeply existential Professor of Theoretical Astrophysics. 

Developed as part of a Machine Learning study in Large Language Models (LLMs), this chatbot utilizes **Prompt Engineering**, **LangChain**, and **Ollama** to create a highly specific and contextual character.

## System Architecture Notes

While this project touches on concepts relevant to **RAG** (Retrieval-Augmented Generation), it primarily focuses on:
1. **Prompt Engineering:** Injecting a dense behavioral guideline into the model prior to user interaction.
2. **Context Window Management:** Iteratively appending `HumanMessage` and `AIMessage` objects to a session state array, which is then passed to the LLM to provide historical conversational context.

## Features

- **Character-Driven Persona**: Uses advanced System Prompting to enforce a strict, consistent character (a weary, sarcastic astrophysicist) that never breaks character or reveals it is an AI.
- **Conversational Memory**: Maintains a running history of the conversation, passing previous context back to the LLM to simulate a natural, ongoing office-hours interaction.
- **Dual Interfaces**: 
  - A responsive, streaming UI built with **Streamlit** (`app.py`).
  - A lightweight Command Line Interface (CLI) for quick terminal testing (`terminal_test.py`).
- **Local Execution**: Runs entirely locally using **Ollama**, ensuring privacy and cost-free inference.

## Tech Stack

- **Python 3.12**
- **Streamlit**: For the web-based graphical user interface.
- **LangChain (langchain-ollama)**: For orchestrating the LLM and managing interaction chains and message memory.
- **Ollama**: For local, on-device model serving (using the `llama3` base model).

## Project Structure

```text
.
├── app.py                  # Main Streamlit web application entry point
├── terminal_test.py        # CLI script for testing the bot in the terminal
├── reqs.txt                # Python dependencies
├── src/
│   ├── core_logic.py       # Core LLM initialization, message handling, and memory logic
│   └── settings.py         # Bot configurations, system prompts, and UI constants
└── static/
    └── zero.png            # Professor Absolute Zero avatar image
```

## Installation & Setup

### 1. Prerequisites
You need to have [Python 3](https://www.python.org/downloads/) and [Ollama](http://ollama.com/) installed on your machine.

If you are on macOS, you can install Ollama via Homebrew:
```bash
brew install ollama
```

### 2. Clone the Repository
```bash
git clone https://github.com/RealSagarBhandari/Professor-Zero-AI-Prof.
cd Professor-Absolute-Zero
```

### 3. Set Up the Python Environment
It is highly recommended to use a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r reqs.txt
```

### 4. Start the Local LLM Server
Open a separate terminal window and start the Ollama service. 
*(If you haven't downloaded the `llama3` model yet, Ollama will automatically pull it on the first run, which may take a few minutes depending on your internet connection).*

```bash
ollama serve
```

##  Usage

### Web Interface
To launch the Streamlit frontend, run:

```bash
streamlit run app.py
```
This will open a new tab in your default web browser at `http://localhost:8501`.

### Terminal Interface
If you prefer a quick text-based interaction without the UI overhead, run:

```bash
python terminal_test.py
```
Type `exit` or `quit` to end the terminal session.



