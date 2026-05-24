# Inquisitive: A personal self-hosted knowledge base with a touch of LLM/RAG

**Inquisitive** is a fully self-hosted LLM/RAG based application that allows you to create your own personal knowledge base which you can easily search and organize.

![Inquisitive](/images/inquisitive-pdf-rendering.png)

![Inquisitive](/images/inquisitive-screenshot.png)

![Inquisitive](/images/inquisitive-markdown-editor.png)

## Features

* Upload files of various formats and store them in vector database for Retrieval-Augmented Generation (RAG)
* Add links/urls whose contents will be fetched automatically and will be added to the vector db
* Add links in bulk
* Crawl a given link recursively (Experimental)
* Add notes in markdown format with the capability to edit/delete later on from the UI itself.
* Focussed mode prompt shortcuts: `/links, /notes, /files` - to narrow down search based on source type.
* streamlit based UI for chat interface
* JWT based auth for basic user management based on fastapi and sqlite
* Multiple vector database backend support - default is `lancedb`.
* Ability to choose between multiple locally installed ollama models from the UI itself
* Listing of reference while discussing with ollama models
* View reference sources inline in case of notes and uploaded file.
* Ability to include/exclude particular references for better focussed search and discussion.
* Ability to select different window size of references - so that one can adjust the context size which will be sent to the llm models

## Installation

### Requirements

* Python 3.11+
* streamlit (for FE UI)
* fastapi (for BE API server)
* Lancedb/ChromaDB (Vector DB)
* Sqlite (Relational DB)
* ollama (locally running ollama instance)

### Ollama Installation
* Please follow the README from [Ollama github page](https://github.com/ollama/ollama)
* What Ollama models to pull?
  * If you've decent gpu consider pulling 7b models like `mistral:7b-instruct-q4_0`. I had good experience with 4b models as well like `gemma3:4b` 
  * If you don't have gpu available, consider pulling 1.5b models like `deepseek-r1:1.5b`, `qwen:1.8b` or `smollm:1.7b`
  * One can pull multiple models as needed and then can select amongst them from the UI
  * for embeddings Inquisitive uses `chroma/all-minilm-l6-v2-f32:latest` - since it is pretty fast for our usecase, but one can change the embedding model if needed from the `backend/config.py`
 

*Install Ollama, pull models and then start the ollama server*

```
$ ollama pull chroma/all-minilm-l6-v2-f32:latest
$ ollama pull mistral:7b-instruct-q4_0
$ ollama pull deepseek-r1:1.5b
$ ollama serve
```

### Install and run backend server and frontend chat interface

* Inquisitive is tested with Python 3.11, 3.12 and 3.13. Make sure any of the python version >= 3.11 is  available on the system.

* On some systems people may need to install `python-venv` package separately. Please install appopriate package on your distro/os as needed.

```
$ python3.11 -m venv venv
$ source venv/bin/activate
$ (venv) git clone https://github.com/kanishka-linux/inquisitive.git
$ (venv) cd inquisitive
$ (venv) pip install -e .
```

*Run backend and FE separately on separate terminals* - This is the preferred approach

```
Make sure you are in the same project directory and venv is activated on both the terminals 

$ (venv) inquisitive-start-backend (Terminal 1)
$ (venv) inquisitive-start-ui (Terminal 2)
```
After that UI will be available at `http://localhost:8501`

*Directly running backend and frontend servers - useful during development*

```
Make sure you are in the project directory and venv is activated

$ (venv) pip install -r requirements.txt
$ (venv) uvicorn backend.main:app --reload --port 8000 --log-level debug

Open Another terminal in the same project directory and activate venv

$ (venv) export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
$ (venv) streamlit run frontend/app.py
```

*Run both BE and FE servers using single command* - experimental

```
$ (venv) inquisitive-start (It will start both BE and FE. Starting BE may take some time on the first run)
```

## Notes on Installation and self-hosting

Inquisitive, is intended to run on your personal computer/laptop and thus it has been designed in such a way that everything can be installed locally as easily as possible. However, depending on where you want to install it some modifications maybe needed for ease of use and better security.

* For installing locally on your local network where security is not a major concern, nothing specific extra is needed and above installation instructions will work as it is, only make sure port 8000 (backend) and port 8501 (Frontend) are available. Use command `$ lsof -i :8501` and `lsof -i :8000` to re-verify nothing is running on the ports before starting the application.

* When installing on a shared network, make sure to setup https for extra layer of security. Please check documentation of uvicorn and streamlit on how to setup https certificates.

* When self-hosting on cloud or some vps provider, make sure to place reverse-proxy like nginx in front of the application and setup https certificate.

* If one wants to self-host Inquisitive for somewhat larger audience number (let's say 50+), then it may require a bit of different deployment strategy and depending on the scale some of the components may require some modifications. Please open github issue or contact via email (provided in the contacts section), in case people want to discuss how to deploy the application for a somewhat larger target audience.

## Config Directory

* When BE and FE server is started for the first time, a config directory is created in the home directory `~/.config/inquisitive`.

* The config directory will have two files `backend.env` and `frontend.env`. People can override default settings by providing new values in the respective env files.
    * For default settings values, take a look at `backend/config.py` and  `frontend/config.py`
    * If user decides to change default base directory or other directory locations using env variables then please make sure to create these directories manually.

* The directory will also have sqlite db and vector database data dir and also uploaded files as well notes. Therefore, it will be good if users can regularly backup the config directory.


## Motivation

Organizing notes and personal documents seems to be a simple task, but I myself struggled a lot with it on how to do it properly. Finally my setup was just plain text/markdown files and open the folder with vim/nvim and use fzf plugin for fuzzy search within the folder.

It served me well over the years, but since last couple of months I was mulling over integration with local LLM/RAG based system for somewhat better organization of personal knowledge base. I looked into existing solutions available, but I couldn't find integrated solutions that would combine notes/local documents/web-links. I was also interested in getting list of references along with a way to display various notes and files inline, so that it will be easier to cross-verify sources from which information is coming. I also felt, the application needs to have some basic authentication capabilities so that one can self-host it, allowing multiple users to share the instance and each having their own unique collection. So After all these requirements in mind, finally I decided to build Inquisitive.

## Technical choices and brief architecture overview

In the beginning, I wanted something simpler which could be built over a weekend, but after one feature after another, things started becoming a bit complex as well as a bit interesting also architecture wise for a self-hosted appllication. For those, who are interested in understanding tech choices and overall architecture, can go thorough the following details.

* **Choic
