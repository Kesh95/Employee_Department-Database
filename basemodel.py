from pydantic import BaseModel
import database
class Item(BaseModel):
    e_name: str
    d_id: int
    salary: int
