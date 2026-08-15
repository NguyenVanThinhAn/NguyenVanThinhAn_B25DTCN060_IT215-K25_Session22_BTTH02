from pydantic import BaseModel, constr, validator
from typing import Literal

class StaffRegister(BaseModel):
    username: str
    password: str
    role: Literal["doctor", "pharmacist"]

class StaffLogin(BaseModel):
    username: str
    password: str
