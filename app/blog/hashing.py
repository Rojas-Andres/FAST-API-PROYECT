from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():
    def bcrypt(password:str):
        hashedpassword = pwd_ctx.hash(password)
        return hashedpassword
    def verify(hashedpassword,plain_password):
        return pwd_ctx.verify(plain_password,hashedpassword)