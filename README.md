
# 🧠 RAG Agent - LinkedIn CV Assistant

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent--Retrieval-brightgreen)](https://www.langchain.dev/)
[![Powered By](https://img.shields.io/badge/Powered%20by-OpenAI-ff69b4?logo=openai)](https://openai.com/)

---

## 🇪🇸 Descripción (Español)

¡Hola! 👋 Este proyecto es un agente conversacional impulsado por **RAG (Retrieval Augmented Generation)**, diseñado para consultar de forma interactiva mi **Currículum Vitae**.

Utiliza técnicas avanzadas de recuperación de información y generación aumentada para responder basándose en un archivo PDF actualizado de mi perfil de LinkedIn.

Pensado especialmente para:
- Reclutadores
- Líderes técnicos
- ¡O cualquier persona curiosa sobre mi trayectoria! 🚀

---

## 🇬🇧 Description (English)

Hello there! 👋 This project is a conversational agent powered by **RAG (Retrieval Augmented Generation)** that lets you interactively explore my **Curriculum Vitae**.

It uses cutting-edge information retrieval and generation techniques, pulling answers from an updated PDF version of my LinkedIn profile.

Designed especially for:
- Recruiters
- Technical leads
- Or anyone curious about my professional journey! 🚀

---

## ⚙️ Technologies Used

- 🐍 **Python 3.10**
- 🔗 **LangChain** (Agent + Retrieval)
- 📚 **FAISS** (Semantic search vector store)
- 🤖 **OpenAI** (LLM for answer generation)
- 🔒 **dotenv** (Environment variables management)
- 🎨 **colorlog** (Pretty, colorful logging)

---

## 🚀 How to Run the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tu_usuario/agentic_rag.git
   cd agentic_rag
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file with the following content:**
   ```bash
   # .env
   HUGGINGFACE_TOKEN=your_token_here
   KNOWLEDGE_FILE_PATH=data/resume.pdf
   LOG_LEVEL=INFO
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

---

## 🧑‍💼 What Can You Ask?

During the interactive session, you can ask questions like:

- "¿Cuál es su experiencia más reciente?" / "What is his most recent experience?"
- "¿Qué tecnologías domina?" / "Which technologies does he master?"
- "¿En qué empresas ha trabajado?" / "Which companies has he worked at?"

👉 To exit, simply type `exit`.

---

## 📚 How It Works

1. Vectorizes the PDF content using **FAISS** 🧠
2. Retrieves the most relevant chunks based on user queries 🔍
3. Generates accurate, grounded answers using **OpenAI LLMs** ✨

> This setup significantly reduces hallucinations and ensures responses are tied to real, verified information.

---

## 📖 Credits & References

This project was built with a lot of help from **ChatGPT** through interactive prompts.
---

## 🧠 Initial System Prompt

<details>
<summary>Click to expand the initial AI prompt used in this project 🔥</summary>

<br>

> You are a helpful, detail-oriented AI assistant collaborating on a Retrieval-Augmented Generation (RAG) project that builds a conversational agent over my LinkedIn CV PDF. We will work phase by phase, and you should never advance to the next phase until I explicitly ask you to. Follow these instructions:

### 📜 Instructions Overview

**1. Phase Awareness**  
- Always begin by summarizing the current phase we are in.  
- Ask if I’m ready to proceed before starting any new phase.

**2. Step-by-Step Reasoning**  
- For each phase or sub-task, break your response into numbered steps.  
- Before writing code or changes, briefly explain your reasoning ("Reasoning: ...").  
- After each step, wait for my confirmation or questions before continuing.

**3. Phases Overview**
- **Phase 1: Logging** – Set up a configurable, color-coded logger that writes to both console and file.  
- **Phase 2: Flexible Configuration** – Centralize all settings (model ID, PDF path, log level) into a `.env` or `config.py`.  
- **Phase 3: Interactive Mode** – Ensure only interactive mode is supported and handle graceful exits.  
- **Phase 4: Advanced RAG Features** – Add conversational memory, query reformulation, multi-step retrieval, source integration, result validation.  
- **Phase 5: Tests & Quality** – Write unit tests, create a Dockerfile, and prepare a polished README.  
- **Phase 6: Deployment** – Dockerize and publish a Gradio/Streamlit demo on Hugging Face Spaces.

**4. Error Handling**  
- If an error or exception is raised during discussion, explain the cause, propose a fix, and wait for my approval before applying it.

**5. User Control**  
- After completing any code snippet or detailed explanation, ask: "Shall we move on to the next step?"  
- Only proceed when I respond with "Yes," "Go ahead," or a similar affirmative.

**6. Final Confirmation**  
- At the end of each phase, provide a brief checklist of what was completed and what remains.  
- Always end with: “Ready for the next phase when you are.”

---

</details>


- **Inspired by Hugging Face's examples on agentic RAG:**  
  👉 [Hugging Face RAG Examples](https://huggingface.co/docs/transformers/agentic_rag)

---

**Thanks for checking it out! Feel free to reach out if you'd like to chat more.** ✨
