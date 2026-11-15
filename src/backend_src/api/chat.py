import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from src.agentic_src.tasks.qa_task import AnswerStructure

from src.backend_src.service.chat import get_answers

logger = logging.getLogger(__name__)
router = APIRouter()

class ChatMessage(BaseModel):
    role : str
    content : str

class ChatHistoryRequest(BaseModel):
    chat_history : List[ChatMessage]

@router.post("/chat/answer")
def chat_answer(request : ChatHistoryRequest):
    logger.info(f"Recieved API Request with chat_history: {request.chat_history}")
    try:
        chat_history = [msg.dict() for msg in request.chat_history]
        result = get_answers(chat_history)
        logger.info(f"API response: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in chat_answer: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))