from sqlalchemy.orm import Session 
from blog.models import *
from fastapi import HTTPException,status
from blog.hashing import Hash


def create_user(request,db:Session):
    if len(request.name) == 0 or len(request.email)==0 or len(request.password)==0:
        return "No se crea usuario , algun campo esta vacio"
    #Hash a la contraseña Hash.bcrypt
    new_user = User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_user(id,response,db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el usuario con el id {id}')
    return user