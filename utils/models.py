import pydantic


class Mood(pydantic.BaseModel):
    mood: float
    text: str
