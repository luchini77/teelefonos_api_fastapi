from sqlalchemy import Column, Integer, String
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