from fastapi import FastAPI
from blog.models import *
from blog.database import engine
from blog.routers import blog,user

app = FastAPI()

Base.metadata.create_all(bind=engine) # Esta linea crea todas las tablas en la base de datos al iniciar la app

#Incluimos todas las rutas 
app.include_router(blog.router)

app.include_router(user.router)

