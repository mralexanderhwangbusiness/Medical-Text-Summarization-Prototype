from fastapi import APIRouter, HTTPException
from summarizer import MedicalTextSummarizer
from models import SummarizationRequest

router = APIRouter()
summarizer = MedicalTextSummarizer()

@router.post("/summarize")
def summarize_text(request: SummarizationRequest):
    try:
        mode = request.mode if hasattr(request, "mode") else "brief"
        summary = summarizer.summarize(request.text, mode)
        return {"summary": summary} if mode == "brief" else summary
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
