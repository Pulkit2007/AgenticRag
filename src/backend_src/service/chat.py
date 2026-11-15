import logging
from src.agentic_src.crew import qa_crew

logger = logging.getLogger(__name__)


def get_answers(chat_history: list) -> dict:
    logger.info(f"Recieved chat history{chat_history}")
    last_user_query = chat_history[-1]
    user_query = last_user_query["content"]
    logger.info(f"Extracted User query{user_query}")

    history_without_last = chat_history[:-1]
    input_data = {"user_query": user_query, "chat_history": history_without_last}

    logging.debug(f"Input data for qa_crew: {input_data}")
    result = qa_crew.kickoff(input_data)
    result_dict = result.to_dict()
    logger.info(f"Result from qa_crew: {result_dict}")
    return result_dict
