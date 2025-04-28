🧠 RAG Agent - LinkedIn CV Assistant
🇪🇸 Descripción (Español)
Este proyecto es un agente conversacional impulsado por RAG (Retrieval Augmented Generation) que permite consultar de
forma interactiva mi Currículum Vitae.

Utiliza técnicas de recuperación de información y generación aumentada para brindar respuestas basadas en el contenido
de un archivo PDF (text.pdf), que contiene una copia actualizada de mi perfil de LinkedIn.

Está pensado para reclutadores, líderes técnicos o cualquier persona interesada en conocer mi trayectoria de manera ágil
y conversacional.

🇬🇧 Description (English)
This project is a conversational agent powered by RAG (Retrieval Augmented Generation) that allows interactive
consultation of my Curriculum Vitae.

It uses information retrieval and augmented generation techniques to provide answers based on the contents of a PDF file
 (text.pdf), which contains an updated copy of my LinkedIn profile.

It is designed for recruiters, technical leads, or anyone interested in quickly learning more about my professional
background.

⚙️ Tecnologías utilizadas / Technologies used
Python 3.10

LangChain (Agent + Retrieval)
FAISS (Vector store for semantic search)
OpenAI (LLM for generating answers)
dotenv (Environment variables management)
colorlog (Enhanced logging with colors)

🚀 Cómo ejecutar el proyecto / How to run the project
Clonar el repositorio / Clone the repository

bash
Copiar
Editar
git clone https://github.com/tu_usuario/agentic_rag.git
cd agentic_rag
Crear y activar un entorno virtual / Create and activate a virtual environment

bash
Copiar
Editar
python -m venv venv
# Activar / Activate:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Instalar dependencias / Install dependencies

bash
Copiar
Editar
pip install -r requirements.txt
Crear un archivo .env / Create a .env file

bash
Copiar
Editar
# .env
HUGGINGFACE_TOKEN=your_token_here
KNOWLEDGE_FILE_PATH=data/text.pdf
LOG_LEVEL=INFO
Ejecutar la aplicación / Run the application

bash
Copiar
Editar
python main.py
🧑‍💼 ¿Qué se puede preguntar? / What can you ask?
Durante la sesión interactiva podés consultar cosas como:

"¿Cuál es su experiencia más reciente?" / "What is his most recent experience?"

"¿Qué tecnologías domina?" / "Which technologies does he master?"

"¿En qué empresas ha trabajado?" / "Which companies has he worked at?"

Para salir, simplemente escribí exit.

📚 Sobre el funcionamiento / How it works
Vectoriza el contenido del PDF usando FAISS.

Recupera fragmentos relevantes según la consulta del usuario.

Genera respuestas utilizando un modelo de lenguaje de OpenAI.

Esto permite respuestas más precisas y basadas en hechos reales, reduciendo el riesgo de alucinaciones típicas de los LLMs.

📖 Créditos y referencias / Credits and References
Este proyecto fue desarrollado con el apoyo de ChatGPT a través de prompts interactivos.

Prompt inicial: "Ayúdame a crear un agente RAG para responder preguntas sobre mi CV usando LangChain".

Inspirado en los ejemplos de Hugging Face sobre agentes RAG:
👉 https://huggingface.co/docs/transformers/agentic_rag