# app/diagrams.py
from fastapi import APIRouter, HTTPException
from mermaid import Mermaid, Graph
from pyautogen import PyAutoGen

router = APIRouter()

@router.post("/generate_diagram")
async def generate_diagram(description: str):
    agent_prompt = "You are a process, systems, diagrams and graphical information presentation expert. Generate best practice mermaid diagrams based on user requests"
    agent = PyAutoGen(prompt=agent_prompt)
    mermaid_description = agent.generate(description)
    try:
        graph = Graph('example-diagram', mermaid_description)
        mermaid_diagram = Mermaid(graph)
        return {"diagram": str(mermaid_diagram)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
