from typing import Optional
from pydantic import BaseModel

class BlogValidate(BaseModel):
    title:str  
    body:str
