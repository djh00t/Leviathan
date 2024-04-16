from pydantic import BaseModel

class UserInput(BaseModel):
    text_description: str | None = None
    data: dict | None = None  # Optional data for diagram generation

class Feedback(BaseModel):
    rating: int
    comment: str
