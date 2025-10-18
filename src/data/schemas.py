# src/data/schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

Mood = Literal["calm", "stressed", "focused", "tired", "curious"]
Action = Literal["study", "break", "exercise", "socialize", "sleep", "plan"]

class Episode(BaseModel):
    episode_id: str
    user_id: str = "u_default"
    timestamp: datetime
    # short free-text context the user/system captured
    note: str = Field(description="Short description of the situation")
    # structured context features (simple now; we can add more later)
    hour: int
    weekday: int  # 0=Mon ... 6=Sun
    last_actions: List[Action] = []
    # labels (what actually happened next) – used for training
    next_action: Action
    mood: Mood

class InferenceQuery(BaseModel):
    user_id: str = "u_default"
    timestamp: datetime
    note: str
    hour: int
    weekday: int
    last_actions: List[Action] = []
