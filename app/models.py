from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
