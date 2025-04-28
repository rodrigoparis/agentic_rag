import datasets

from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from utils.logger import logger


def load_documents_from_local(file_path: str):
    logger.info("*** 📄 Loading knowledge base...")
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    elif file_path.endswith(".md"):
        loader = UnstructuredMarkdownLoader(file_path)
    else:
        raise ValueError("Formato de archivo no sportoado")
    logger.info("*** Knowledge base loaded!")

    return loader.load()


def prepare_knowledge_base(file_path="data/my_doc.pdf"):
    logger.info("*** Preparing knowledge base...")
    documents = load_documents_from_local(file_path)


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap=0,
        separators=["\n\n", "\n", " ", ""],
    )

    logger.info("*** Spliting documents...")
    docs = text_splitter.split_documents(documents)
    logger.info("*** The documents are splitted!")

    logger.info("*** Getting embeddings from HuggingFace...")
    embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-small")
    logger.info("*** We got the embeddings!")

    logger.info("*** Getting the vector_store with the documents and embeddings...")
    vector_store = FAISS.from_documents(docs, embeddings)
    logger.info("*** Knowledge base prepared!")

    return vector_store