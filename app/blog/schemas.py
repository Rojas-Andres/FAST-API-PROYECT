from typing import Optional , List
from pydantic import BaseModel

class BlogValidate(BaseModel):
    title:str  
    body:str
    class Config():
        orm_mode = True
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

class ShowUserCreate(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True
class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[BlogValidate] = [] # Es una lista de blogs ya que trae todos
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email:Optional[str]=None