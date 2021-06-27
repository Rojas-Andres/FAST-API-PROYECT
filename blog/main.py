from fastapi import FastAPI,Depends
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


@app.post('/blog')
def create(blog:BlogValidate,db:Session=Depends(get_db)):
    new_blog = Blog(title=blog.title,body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    #return {'Title':blog.title , 'Body':blog.body}