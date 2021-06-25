from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return 'hola'

@app.get('/retorna_json')
def retorna_json():
    return {"data":{"name":"andres"}}