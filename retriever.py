from smolagents import Tool

class RetrieverTool(Tool):
    name = "retriever"
    description = (
        "Busca en la base de conocimiento usando FAISS y devuelve el texto."
    )
    inputs = {
        "query": {
             "type": "string",
             "description": "Pregunta para buscar en la base de conocimiento."
    }}
    output_type = "string"

    def __init__(self, vectordb, **kwargs):
        super().__init__(**kwargs)
        self.vectordb = vectordb

    def forward(self, query: str) -> str:
        docs = self.vectordb.similarity_search(query, k=5)
        return "\n\n".join([doc.page_content for doc in docs])
