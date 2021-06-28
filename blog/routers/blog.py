from fastapi import APIRouter,Depends,Response,HTTPException,status
from typing import List
from blog.schemas import *
from blog.models import *
from blog.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


#Obtener todos los blog
@router.get('/blog', response_model = List[ShowBlog],tags=['blogs']) # Es una lista porque vamos a retornar multiples blogs no solo uno 
def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

#Crear un blog
@router.post('/blog', status_code=status.HTTP_201_CREATED,tags=['blogs']) # Devolvemos el estatus de 201 que es generalmente cuando se crea 
def create(blog:BlogValidate,db:Session=Depends(get_db)):
    new_blog = Blog(title=blog.title,body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    #return {'Title':blog.title , 'Body':blog.body}

#Eliminar un blog
@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def destroy(id,db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id} por lo tanto no se elimino')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Realizado'

#Actualizar blog
@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id,request:BlogValidate ,db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    print(blog)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id} por lo tanto no se actualizo')
    #blog.update(request)
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'Actualizado'

#Obtener un blog
@router.get('/blog/{id}',status_code=200 , response_model=ShowBlog,tags=['blogs'])
def show(id, response:Response, db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        '''
        
        Hay varias maneras de manejar que no encuentr el id 

        '''
        # Manera 1
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id}')
        # Manera 2
        '''
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detalle':f'No existe el blog con el id {id}'}
        '''
    return blog