from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from config.base_datos import base

class Telefono(base):
    __tablename__='telefonos'
    id = Column(Integer, primary_key=True)
    nivel = Column(String)
    ubicacion = Column(String)
    telefono = Column(String)
    num_telefono = Column(String)
    estado = Column(String)
    informacion = Column(String)
    creada = Column(DateTime(timezone=True), server_default=func.now())
    actualizada = Column(DateTime(timezone=True), onupdate=func.now())