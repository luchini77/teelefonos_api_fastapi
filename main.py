from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

from config.base_datos import base, motor
from routes.telefonos import router_fono


app = FastAPI()
app.title = 'App de Telefonos 208'
app.version = '1.0.1'

#PARA SQLITE
base.metadata.create_all(bind=motor)


#INICIO
@app.get('/', tags=['Inicio'])
def mensaje():
    return HTMLResponse('<h2>Api de Telefonos</h2>')


app.include_router(router_fono)



if __name__ == '__main__':
    uvicorn.run('main:app',port=8000,reload=True)