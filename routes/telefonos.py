from fastapi import APIRouter, Body, Path, Query, Request, HTTPException, Depends, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from sqlalchemy.orm import Session

from repositorio import crud
#from models.telefono_modelo import Telefono as TelModel
from schema.telefono_schema import TelefonoUpdate, Telefono as TelSche
from config.base_datos import sesion, motor, base, get_db


router_fono = APIRouter(prefix='/telefono', tags=['Telefono'])


#EL CRUD DE LOS TELEFONOS

#TODOS LOS TELEFONOS
@router_fono.get('/', status_code=status.HTTP_200_OK)
def todos_telefonos(db: Session=Depends(get_db)):
    telefonos = crud.get_all(db)
    return telefonos

#BUSCAR UN SOLO TELEFONO
@router_fono.get('/{id}', status_code=status.HTTP_200_OK)
def un_telefono(id:int = Path(ge=1), db: Session=Depends(get_db)):
    telefono = crud.get_by_id(id, db)
    return telefono

#AGREGAR UN TELEFONO
@router_fono.post('/', status_code=status.HTTP_201_CREATED)
def agregar_telefono(telefono: TelSche, db: Session=Depends(get_db)):
    telefono = crud.create(telefono, db)
    return {'respuesta': 'telefono creado exitosamente!'}

#ACTUALIZA UN TELEFONO
@router_fono.put('/{id}', status_code=status.HTTP_200_OK)
def actualiza_telefono(id:int, update_fono: TelefonoUpdate, db: Session=Depends(get_db)):
    respuesta = crud.actualizar(id, update_fono, db)
    return respuesta

#ELIMINAR UN TELEFONO
@router_fono.delete('/{id}', status_code=status.HTTP_200_OK)
def borrar_telefono(id:int, db: Session=Depends(get_db)):

    respuesta = crud.delete(id, db)
    return respuesta