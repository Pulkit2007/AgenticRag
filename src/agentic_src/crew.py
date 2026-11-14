from crewai import Crew

from src.agentic_src.agents.question_answer import qa_agent
from src.agentic_src.tasks.qa_task import qa_task


qa_crew = Crew(
    agents=[qa_agent],
    tasks=[qa_task],
    verbose=True,
)