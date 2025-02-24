from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
    mode: str = "brief"  # Default mode is "brief", can be "json"
