from fastapi import APIRouter,Depends,HTTPException,status
from blog.schemas import Login
from blog.database import *
from sqlalchemy.orm import Session
from blog.models import *
from blog.hashing import Hash
from blog.token import *
router = APIRouter(
    prefix='/login',
    tags=['Login']
)

@router.post('/')
def login(request:Login,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email==request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Credenciales invalidas')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Credenciales invalidas')
        #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
