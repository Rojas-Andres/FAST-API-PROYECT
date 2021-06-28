from sqlalchemy.orm import Session 
from blog.models import *
from fastapi import HTTPException,status

def get_all(db:Session):
    blogs = db.query(Blog).all()
    return blogs

def create_blog(blog,db:Session):
    new_blog = Blog(title=blog.title,body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy_blog(id:int,db:Session):
    blog = db.query(Blog).filter(Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id} por lo tanto no se elimino')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Realizado'

def update_blog(id:int,request,db:Session):
    blog = db.query(Blog).filter(Blog.id == id)
    print(blog)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id} por lo tanto no se actualizo')
    #blog.update(request)
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'Actualizado'

def get_one_blog(id,response,db):
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