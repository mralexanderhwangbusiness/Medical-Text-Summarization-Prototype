from fastapi import APIRouter, HTTPException
from app.summarizer import MedicalTextSummarizer
from app.models import SummarizationRequest

router = APIRouter()
summarizer = MedicalTextSummarizer()

@router.post("/summarize")
def summarize_text(request: SummarizationRequest):
    try:
        summary = summarizer.summarize(request.text)
        return {"summary": summary}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
