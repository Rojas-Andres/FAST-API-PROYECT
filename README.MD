# Instalar todos los paquetes necesarios

pip install -r requeriments.txt

# Como iniciar proyecto ?
    # Esto lo que hace es iniciar el servidor y cada cambio que realicemos en nuestra app se vera al instante ya que el servidor se reinicia solo 
    - uvicorn main:app --reload
    - main = Al nombre del archivo 
    - app = es la instancia de FastAPI

# FastAPI tiene integrado una interfaz para las peticiones
    -  la ruta se encuentra en http://127.0.0.1:8000/docs (Teniendo en cuenta que estamos en localhost ) alli veremos las peticiones

# Query params
    -  La api tiene un limitante por peticion y debe de cumplir algunas condiciones , ejemplo : La api va a devolver solamente los 10 blogs publicados que se encuentren en true
    -  para mas informacion leer la doc https://fastapi.tiangolo.com/tutorial/query-params/

# Prueba de blog enviando params
    - Published es un boolean
    http://localhost:8000/blog?limit=10&published=false