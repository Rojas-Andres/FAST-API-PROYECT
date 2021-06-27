------ La base de datos del proyecto es SQLite para que se pueda replicar facilmente --------


# Crear un entorno virtual
Primero instalar virtualenv

pip install virtualenv
o
pip3 install virtualenv

Crear el entorno virtual
- virtualenv venv 

Activar el entorno virtual en windows

- .\venv\Scripts\activate.bat

# Instalar todos los paquetes necesarios

pip install -r requirements.txt
o
pip3 install -r requirements.txt

# Como iniciar proyecto ?
    # Esto lo que hace es iniciar el servidor y cada cambio que realicemos en nuestra app se vera al instante ya que el servidor se reinicia solo 
    - uvicorn main:app --reload
    - main = Al nombre del archivo 
    - app = es la instancia de FastAPI

    - Como Correr fastapi de main ? 
        - uvicorn blog.main:app --reload

# Segunda forma de iniciar el proyecto para depuracion del codigo .
    - colocando esto en nuestro archivo main.py lo unico que tenemos que hacer es ejecutar
    python main.py (teniendo en cuenta que tenemos la version 3 ) si no python3 main.py y ya , no es necesario uvicorn main:app --reload, este
    caso seria solamente para depurar el codigo
    
    if __name__ == "__main__":
        uvicorn.run(app,host="127.0.0.1", port=9000)

# FastAPI tiene integrado una interfaz para las peticiones
    -  la ruta se encuentra en http://127.0.0.1:8000/docs (Teniendo en cuenta que estamos en localhost ) alli veremos las peticiones

# Query params
    -  La api tiene un limitante por peticion y debe de cumplir algunas condiciones , ejemplo : La api va a devolver solamente los 10 blogs publicados que se encuentren en true
    -  para mas informacion leer la doc https://fastapi.tiangolo.com/tutorial/query-params/

# Prueba de blog enviando params
    - Published es un boolean
    http://localhost:8000/blog?limit=10&published=false

Envio de params por el request body
    - Se necesita pydentic y importar BaseModel