from fastapi import FastAPI
from typing import Optional
from models_params import Blog
app = FastAPI()


'''

Rutas de prueba , si desean comentan 

'''
@app.get('/hello')
def hello():
    return 'hola'

@app.get('/retorna_json')
def retorna_json():
    return {"data":{"name":"andres"}}


'''

Rutas del proyecto

'''

@app.get('/blog') 
def index(limit=10 , published:bool=True , sort: Optional[str] = None ): #valores predeterminados y el sort puede ser opcional
    if published:
        # Solo obtiene los 10 blogs publicados
        return {'data':f'{limit} publicados blogs en la bd '}
    else: 
        return {'data':f'{limit} blogs en la bd '}
@app.get('/blog/unpublished')
def unpublished():
    # Obtener los blogs que no estan publicados
    return {"data":"Aun no estan publicados"}

@app.get('/blog/{id}')
def blog(id:int): #Con esto le decimos que debe de ser estrictamente int
    # Obtener blog con el id = id
    return {"data":id}

@app.get('/blog/{id}/comments')
def blog(id,limit=10):
    # Obtener comentarios del blog con el id = id
    return {"data": [1,2 ] }

@app.post('/blog')
def create_blog(blog:Blog): # El objeto es de la clase Blog que definimos con anterioridad
    return {'data':f' El blog fue creado n {blog.title}'}