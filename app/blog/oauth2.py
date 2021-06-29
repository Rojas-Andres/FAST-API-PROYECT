from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends,HTTPException,status
from blog.token import create_access_token,verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")# login es la ruta donde se buscara el token -> validar si el usuario ya esta logueado

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    verify_token(token,credentials_exception)