from smolagents import HfApiModel, CodeAgent
from utils.logger import logger
from tools import search_tool
from retriever import RetrieverTool


def build_agent(vectordb):
    logger.info("🛠️ Agent build started.")
    model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")  # o cualquier otro modelo HF

    retriever = RetrieverTool(vectordb=vectordb)

    agent = CodeAgent(
        tools=[retriever, search_tool],
        model=model,
        add_base_tools=True,
        planning_interval=3,
        reset=False
    )
    return agent
