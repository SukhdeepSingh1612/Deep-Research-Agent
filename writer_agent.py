from pydantic import BaseModel, Field
from agents import Agent
from typing import List


writer_instructions = ( "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 5-10 pages of content, at least 1000 words."
)

class ReportData(BaseModel):
    short_summary: str = Field(description="A short summary of the report")

    markdown_report: str = Field(description="The report in markdown format")

    follow_up_questions: List[str] = Field(description="A list of follow-up questions that the reader may have")

writer_agent = Agent(
    name="Writer agent",
    instructions=writer_instructions,
    model="gpt-4o-mini",
    output_type=ReportData,
)