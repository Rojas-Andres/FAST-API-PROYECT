from fastapi import FastAPI
from blog.schemas import BlogValidate
from blog.models import *
from blog.database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine) # Esta linea crea todas las tablas en la base de datos al iniciar la app
@app.post('/blog')
def create(blog:BlogValidate):
    return {'Title':blog.title , 'Body':blog.body}