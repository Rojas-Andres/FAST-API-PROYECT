from fastapi import APIRouter,Depends,Response,HTTPException,status
from blog.schemas import *
from blog.models import *
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.hashing import Hash

router = APIRouter()

@router.post('/user',response_model=ShowUserCreate,tags=['users'])
def create_user(request:UserValidate,db:Session=Depends(get_db)):
    if len(request.name) == 0 or len(request.email)==0 or len(request.password)==0:
        return "No se crea usuario , algun campo esta vacio"
    #Hash a la contraseña Hash.bcrypt
    new_user = User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}',status_code=200 , response_model=ShowUser,tags=['users'])
def show(id:int, response:Response, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el usuario con el id {id}')
    return user