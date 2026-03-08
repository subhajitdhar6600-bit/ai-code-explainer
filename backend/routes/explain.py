from fastapi import APIRouter
from services.ai_service import explain_repository, summarize_repository
from models.repo_request import RepoRequest

router = APIRouter()

@router.post("/explain")
def explain_repo(request: RepoRequest):
    explanation = explain_repository(request.repo_url)
    return {"explanation": explanation}

@router.post("/summarize")
def summarize_repo(request: RepoRequest):
    summary = summarize_repository(request.repo_url)
    return {"summary": summary}