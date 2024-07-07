from langchain_core.pydantic_v1 import BaseModel, Field

class Discussion(BaseModel):
   question: list[str] = Field(description='List of discussion question')
   answer: list[str] = Field(description='List of answers corresponding to the questions')


