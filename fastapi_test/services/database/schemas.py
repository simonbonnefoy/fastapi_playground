from typing import Optional

from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
    email: str