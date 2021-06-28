from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog.schemas import *
from blog.models import *
from blog.database import engine,SessionLocal
from sqlalchemy.orm import Session
from blog.hashing import Hash
app = FastAPI()

Base.metadata.create_all(bind=engine) # Esta linea crea todas las tablas en la base de datos al iniciar la app

#Conexion
def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()

#Crear un blog
@app.post('/blog', status_code=status.HTTP_201_CREATED,tags=['blogs']) # Devolvemos el estatus de 201 que es generalmente cuando se crea 
def create(blog:BlogValidate,db:Session=Depends(get_db)):
    new_blog = Blog(title=blog.title,body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    #return {'Title':blog.title , 'Body':blog.body}

#Eliminar un blog
@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def destroy(id,db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id )
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id} por lo tanto no se elimino')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Realizado'

#Actualizar blog
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id,request:BlogValidate ,db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    print(blog)
    if not blog.first(): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el blog con el id {id} por lo tanto no se actualizo')
    #blog.update(request)
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'Actualizado'

#Obtener todos los blog
@app.get('/blog', response_model = List[ShowBlog],tags=['blogs']) # Es una lista porque vamos a retornar multiples blogs no solo uno 
def get_all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

#Obtener un blog
@app.get('/blog/{id}',status_code=200 , response_model=ShowBlog,tags=['blogs'])
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

@app.post('/user',response_model=ShowUserCreate,tags=['users'])
def create_user(request:UserValidate,db:Session=Depends(get_db)):
    if len(request.name) == 0 or len(request.email)==0 or len(request.password)==0:
        return "No se crea usuario , algun campo esta vacio"
    #Hash a la contraseña Hash.bcrypt
    new_user = User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',status_code=200 , response_model=ShowUser,tags=['users'])
def show(id:int, response:Response, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el usuario con el id {id}')
    return user