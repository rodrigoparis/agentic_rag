import sys

from auth import authenticate
from agent import build_agent
from knowledge_base import prepare_knowledge_base
from utils.logger import logger
from utils.config import Config


def main():

    logger.info("🚀 Started application in interactive mode.")
    try:
        authenticate()
        vector_store = prepare_knowledge_base(file_path=Config.KNOWLEDGE_FILE_PATH)
        agent = build_agent(vector_store)
        while True:
            question = input("Do me a question or write 'exit': ")
            if question.lower() == "exit":
                logger.info("👋 Session ended by user.")
                print("\nThank you for chatting with me! 🚀")
                print("If you'd like to connect, feel free to reach out via LinkedIn:")
                print("🔗 https://www.linkedin.com/in/rodrigo-paris-bna/\n")
                break
            logger.info(f"🧑 User Question: {question}")
            response = agent.run(question)
            logger.info(f"🤖 Agent Response: {response}")
    except Exception as e:
        logger.error(f"🔥 Error during main execution", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
