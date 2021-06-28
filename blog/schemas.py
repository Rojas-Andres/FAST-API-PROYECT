from typing import Optional
from pydantic import BaseModel

class BlogValidate(BaseModel):
    title:str  
    body:str

#Opcion 1
'''

class ShowBlog(BlogValidate):
    class Config():
        orm_mode = True

'''
#Opcion 2
class ShowBlog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True