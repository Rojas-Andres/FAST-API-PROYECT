from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog.schemas import BlogValidate
from blog.models import *
from blog.database import engine,SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

Base.metadata.create_all(bind=engine) # Esta linea crea todas las tablas en la base de datos al iniciar la app

def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED) # Devolvemos el estatus de 201 que es generalmente cuando se crea 
def create(blog:BlogValidate,db:Session=Depends(get_db)):
    new_blog = Blog(title=blog.title,body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    #return {'Title':blog.title , 'Body':blog.body}

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id ).delete(synchronize_session=False)
    db.commit()
    return 'Realizado'


@app.get('/blog')
def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200)
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