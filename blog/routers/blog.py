from fastapi import APIRouter,Depends,Response,HTTPException,status
from typing import List
from blog.schemas import *
from blog.models import *
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.repository import blog
from blog.oauth2 import get_current_user
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


#Obtener todos los blog
@router.get('/', response_model = List[ShowBlog]) # Es una lista porque vamos a retornar multiples blogs no solo uno 
def get_all_blogs(db:Session=Depends(get_db),current_user:User =Depends(get_current_user)):
    return blog.get_all(db)

#Crear un blog
@router.post('/', status_code=status.HTTP_201_CREATED) # Devolvemos el estatus de 201 que es generalmente cuando se crea 
def create(request:BlogValidate,db:Session=Depends(get_db) ,get_current_user:User =Depends(get_current_user) ):
    return blog.create_blog(request,db)

#Eliminar un blog
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):

    return blog.destroy_blog(id,db)

#Actualizar blog
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:BlogValidate ,db:Session=Depends(get_db)):
    return blog.update_blog(id,request,db)

#Obtener un blog
@router.get('/{id}',status_code=200 , response_model=ShowBlog)
def show(id, response:Response, db:Session=Depends(get_db)):
    return blog.get_one_blog(id,response,db)