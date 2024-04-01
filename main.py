from pydantic import BaseModel
from typing import List
class User(BaseModel):
    username: str
    mail: str
    address: str
class Banks(BaseModel):
    name: str
    rating: float
    opened: int

class Cards(BaseModel):
    cardholder: User
    which_bank: List[Banks]
    opened: int

class Balance(BaseModel):
    card: List[Cards]
    amount: int
    currency: int




