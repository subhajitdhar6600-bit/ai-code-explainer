from fastapi import FastAPI
from routes.explain import router as explain_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Code Explainer Backend Running"}

app.include_router(explain_router)