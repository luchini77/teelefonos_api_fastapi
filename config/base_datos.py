import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


fichero = "./datos_telefonos.sqlite"

directorio = 'BBDD/'

ruta = f"sqlite:///{os.path.join(directorio, fichero)}"

motor = create_engine(ruta, echo=True)

sesion = sessionmaker(bind=motor)

base = declarative_base()

def get_db():
    db = sesion()
    try:
        yield db
    finally:
        db.close()