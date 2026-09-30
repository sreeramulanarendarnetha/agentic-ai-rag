\# 🤖 Agentic AI RAG Assistant



<p align="center">



\*\*A local Agentic AI question-answering system powered by RAG, LangGraph, Pinecone, Hugging Face embeddings, and Ollama.\*\*



<br>



<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white" alt="Python">

<img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge" alt="LangChain">

<img src="https://img.shields.io/badge/LangGraph-Workflow-1C3C3C?style=for-the-badge" alt="LangGraph">

<img src="https://img.shields.io/badge/Pinecone-Vector\_DB-000000?style=for-the-badge" alt="Pinecone">

<img src="https://img.shields.io/badge/Ollama-Llama\_3.2-black?style=for-the-badge" alt="Ollama">

<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white" alt="Streamlit">



</p>



\---



\## 🌟 Overview



\*\*Agentic AI RAG Assistant\*\* is a Retrieval-Augmented Generation application that allows users to ask questions about an \*\*Agentic AI ebook\*\*.



Instead of sending the entire document to an LLM, the system:



1\. 📄 Loads the PDF document.

2\. ✂️ Splits it into smaller chunks.

3\. 🧠 Generates local vector embeddings.

4\. 📦 Stores the vectors in Pinecone.

5\. 🔎 Retrieves the most relevant chunks for a question.

6\. 🔗 Orchestrates retrieval and generation with LangGraph.

7\. 🤖 Generates an answer using local \*\*Llama 3.2\*\* through Ollama.

8\. 📊 Returns a confidence score.

9\. 🖥️ Displays the result through Streamlit.



\---



\## ✨ Key Features



| Feature               | Description                                   |

| --------------------- | --------------------------------------------- |

| 📄 PDF Processing     | Loads the Agentic AI ebook using PyPDFLoader  |

| ✂️ Smart Chunking     | Uses recursive character-based text splitting |

| 🧠 Local Embeddings   | Uses `all-MiniLM-L6-v2`                       |

| 📦 Vector Database    | Stores document vectors in Pinecone           |

| 🔎 Semantic Search    | Retrieves the most relevant document chunks   |

| 🔗 LangGraph          | Manages the RAG workflow                      |

| 🤖 Local LLM          | Uses Llama 3.2 through Ollama                 |

| 📊 Confidence         | Extracts a model-generated confidence score   |

| 🖥️ Web UI            | Interactive Streamlit interface               |

| 💰 Low API Dependency | Embeddings and generation run locally         |



\---



\## 🏗️ System Architecture



```text

&#x20;                    ┌──────────────────────┐

&#x20;                    │   Agentic AI Ebook   │

&#x20;                    │        PDF           │

&#x20;                    └──────────┬───────────┘

&#x20;                               │

&#x20;                               ▼

&#x20;                    ┌──────────────────────┐

&#x20;                    │    PyPDFLoader       │

&#x20;                    │    PDF Extraction    │

&#x20;                    └──────────┬───────────┘

&#x20;                               │

&#x20;                               ▼

&#x20;                    ┌──────────────────────┐

&#x20;                    │ Text Splitter        │

&#x20;                    │ 1000 chars           │

&#x20;                    │ 200 overlap           │

&#x20;                    └──────────┬───────────┘

&#x20;                               │

&#x20;                               ▼

&#x20;             ┌─────────────────────────────────┐

&#x20;             │ Hugging Face Embeddings         │

&#x20;             │ all-MiniLM-L6-v2                │

&#x20;             │ 384 dimensions                  │

&#x20;             └───────────────┬─────────────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                   ┌───────────────────┐

&#x20;                   │     Pinecone      │

&#x20;                   │   Vector Store    │

&#x20;                   └─────────┬─────────┘

&#x20;                             │

&#x20;                        User Question

&#x20;                             │

&#x20;                             ▼

&#x20;                   ┌───────────────────┐

&#x20;                   │     Retriever     │

&#x20;                   │     Top-K = 4     │

&#x20;                   └─────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                   ┌───────────────────┐

&#x20;                   │    LangGraph      │

&#x20;                   │                   │

&#x20;                   │ retrieve → generate│

&#x20;                   └─────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                   ┌───────────────────┐

&#x20;                   │   Ollama + Llama  │

&#x20;                   │       3.2         │

&#x20;                   └─────────┬─────────┘

&#x20;                             │

&#x20;                             ▼

&#x20;                   ┌───────────────────┐

&#x20;                   │ Answer + Confidence│

&#x20;                   └───────────────────┘

```



\---



\## 🧩 LangGraph Workflow



The application uses a simple two-node LangGraph workflow:



```text

&#x20;       START

&#x20;         │

&#x20;         ▼

&#x20;  ┌─────────────┐

&#x20;  │   retrieve  │

&#x20;  └──────┬──────┘

&#x20;         │

&#x20;         ▼

&#x20;  ┌─────────────┐

&#x20;  │   generate  │

&#x20;  └──────┬──────┘

&#x20;         │

&#x20;         ▼

&#x20;        END

```



\### 🔎 `retrieve`



The retrieval node:



\* Receives the user's question.

\* Searches Pinecone.

\* Retrieves the top 4 relevant document chunks.

\* Combines the chunks into the context.



\### 🤖 `generate`



The generation node:



\* Receives the question and retrieved context.

\* Sends them to Llama 3.2.

\* Instructs the model to use only the retrieved context.

\* Avoids unsupported information.

\* Produces an answer.

\* Extracts a confidence score.



\---



\## 📁 Project Structure



```text

rag-agentic-ai/

│

├── 📂 data/

│   └── 📄 Ebook-Agentic-AI.pdf

│

├── 📂 src/

│   ├── 🐍 \_\_init\_\_.py

│   ├── 🐍 config.py

│   ├── 🐍 ingestion.py

│   └── 🐍 graph.py

│

├── 🖥️ app.py

├── 🧪 tests\_sample\_queries.py

├── 📦 requirements.txt

├── 🔐 .env

├── 🔐 .env.example

└── 📖 README.md

```



\---



\## 📊 Current Dataset



The current ebook ingestion produced:



```text

📄 Pages              : 60

🧩 Chunks             : 119

📐 Embedding Dimension: 384

📦 Pinecone Vectors   : 119

📏 Distance Metric    : cosine

🔢 Retriever Top-K    : 4

```



\### Embedding Model



```text

sentence-transformers/all-MiniLM-L6-v2

```



\### LLM



```text

Llama 3.2

```



\### LLM Runtime



```text

Ollama

```



\---



\# 🚀 Getting Started



\## 1️⃣ Prerequisites



Make sure you have:



\* Python 3.11+

\* Pinecone account/API key

\* Ollama

\* Llama 3.2

\* Git (optional)



\---



\## 2️⃣ Open the Project



```cmd

cd C:\\Users\\Narendar\\Desktop\\rag-agentic-ai

```



\---



\## 3️⃣ Activate Virtual Environment



```cmd

venv\\Scripts\\activate

```



You should see:



```text

(venv) C:\\Users\\Narendar\\Desktop\\rag-agentic-ai>

```



\---



\## 4️⃣ Install Dependencies



```cmd

pip install -r requirements.txt

```



\---



\## 5️⃣ Configure Environment Variables



Create `.env`:



```text

OPENAI\_API\_KEY=your\_openai\_api\_key

PINECONE\_API\_KEY=your\_pinecone\_api\_key

PINECONE\_INDEX\_NAME=ebook-agentic-ai

PINECONE\_CLOUD=aws

PINECONE\_REGION=us-east-1

```



> \*\*Security:\*\* Never commit your real `.env` file or API keys to GitHub.



\---



\# 📚 Document Ingestion



Place the ebook here:



```text

data/Ebook-Agentic-AI.pdf

```



Run:



```cmd

python src\\ingestion.py

```



The pipeline performs:



```text

PDF

&#x20;↓

PyPDFLoader

&#x20;↓

RecursiveCharacterTextSplitter

&#x20;↓

Hugging Face Embeddings

&#x20;↓

Pinecone

```



\### Current Chunk Configuration



```python

chunk\_size = 1000

chunk\_overlap = 200

```



\---



\# 🦙 Ollama Setup



Install Ollama and verify:



```cmd

ollama --version

```



Download Llama 3.2:



```cmd

ollama pull llama3.2

```



Verify the model:



```cmd

ollama list

```



You should see:



```text

llama3.2

```



\---



\# 🖥️ Run the Application



Start Streamlit:



```cmd

streamlit run app.py

```



Then open:



```text

http://localhost:8501

```



You can ask questions such as:



```text

What is agentic AI?

```



```text

What are the characteristics of agentic AI?

```



```text

How do AI agents make decisions?

```



\---



\# 🧪 Run Sample Tests



Run:



```cmd

python tests\_sample\_queries.py

```



The test script sends several questions through the complete LangGraph RAG pipeline.



\---



\# 🔍 Verify Pinecone



To check the stored vectors:



```cmd

python -c "from dotenv import load\_dotenv; import os; from pinecone import Pinecone; load\_dotenv(); pc=Pinecone(api\_key=os.getenv('PINECONE\_API\_KEY')); index=pc.Index(os.getenv('PINECONE\_INDEX\_NAME')); print(index.describe\_index\_stats())"

```



Expected information includes:



```text

dimension: 384

metric: cosine

total\_vector\_count: 119

```



\---



\# 🛠️ Troubleshooting



\## Ollama is not recognized



If you see:



```text

'ollama' is not recognized as an internal or external command

```



Install Ollama and restart your terminal.



Then run:



```cmd

ollama --version

```



\---



\## Streamlit `torchvision` Warning



If Streamlit displays repeated errors related to:



```text

ModuleNotFoundError: No module named 'torchvision'

```



you can disable Streamlit's file watcher:



```cmd

streamlit run app.py --server.fileWatcherType none

```



This application uses text embeddings and does not require image processing for its RAG workflow.



\---



\## Hugging Face Authentication Warning



You may see:



```text

You are sending unauthenticated requests to the HF Hub.

```



This is a warning about Hugging Face Hub authentication and does not necessarily indicate that the application failed.



\---



\# 🔐 Security



Do \*\*not\*\* upload these files to GitHub:



```text

.env

```



Your `.gitignore` should contain:



```gitignore

.env

venv/

\_\_pycache\_\_/

\*.pyc

.streamlit/secrets.toml

```



\---



\# 🎯 Project Goals



This project demonstrates practical implementation of:



\* Retrieval-Augmented Generation

\* Vector databases

\* Semantic search

\* Local embedding models

\* Local LLM inference

\* LangGraph workflows

\* Prompt-based generation

\* Confidence extraction

\* Streamlit application development



\---



\# 🧰 Technology Stack



```text

Python

&#x20;  │

&#x20;  ├── LangChain

&#x20;  ├── LangGraph

&#x20;  ├── PyPDF

&#x20;  ├── Hugging Face

&#x20;  ├── Sentence Transformers

&#x20;  ├── Pinecone

&#x20;  ├── Ollama

&#x20;  ├── Llama 3.2

&#x20;  └── Streamlit

```



\---



\# 📌 Future Improvements



Potential extensions include:



\* 💬 Chat history

\* 📚 Multiple PDF support

\* 🔎 Source citation display

\* 🧠 Query rewriting

\* 🔀 Conditional LangGraph routing

\* 📊 Retrieval evaluation

\* 📝 Conversation memory

\* 🚀 Deployment

\* 🔐 Authentication

\* 📈 RAG evaluation metrics



\---



\# 👨‍💻 Author



\*\*Narendar Sreeramula\*\*



B.Tech — Computer Science \& Engineering (Data Science)



\---



<p align="center">



\### ⭐ If you found this project useful, consider starring the repository!



\*\*Built with Python • LangChain • LangGraph • Pinecone • Ollama • Streamlit\*\*



</p>



"# agentic_ai-rag" 
