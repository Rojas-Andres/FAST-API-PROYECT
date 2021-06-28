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


class UserValidate(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode = True