from pydantic import BaseModel
from typing import Optional


class Telefono(BaseModel):
    nivel: str
    ubicacion: str
    telefono: str
    num_telefono: str
    estado: str
    informacion: str

    class Config:
        from_atributes=True
        json_schema_extra = {
            'example':{
                'nivel':'UCL',
                'ubicacion':'xc 8',
                'telefono':'2',
                'num_telefono':'2345',
                'estado':'operativo',
                'informacion':'sin novedad'
            }
        }

class TelefonoUpdate(BaseModel):
    nivel: str = None
    ubicacion: str = None
    telefono: str = None
    num_telefono: str = None
    estado: str = None
    informacion: str = None