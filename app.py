#  2026 Julius Cameron Hill / TitanU AI LLC. All rights reserved. Patent pending JCH-2026-001.
from fastapi import FastAPI
from agent import CreativeWritingCoAuthorAgent

app = FastAPI(title="TitanU - Creative-Writing-CoAuthor")
agent = CreativeWritingCoAuthorAgent()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
