from pydantic import BaseModel, Field
from agents import Agent

number_of_searches = 3

class WebSearchItem(BaseModel):
    reason: str = Field(description="The reason for the search")
    query: str = Field(description="The query to search for")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="The list of search items")


planner_instructions = f"You are a helpful research assistant. Given a query, come up with a set of web searches \
to perform to best answer the query. Output {number_of_searches} terms to query for."


planner_agent = Agent(name="plannerAgent", instructions=planner_instructions,model="gpt-4o-mini", output_type=WebSearchPlan)