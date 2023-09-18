from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.telefono_modelo import Telefono
from schema.telefono_schema import Telefono as Fono


def get_all(db: Session):
    telefonos = db.query(Telefono).all()

    return telefonos


def get_by_id(id: int, db: Session):
    telefono = db.query(Telefono).get(id)

    if telefono is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return telefono


def create(telefono, db: Session):
    telefono = telefono.dict()
    try:
        new_telefono = Telefono(
            nivel=telefono['nivel'], 
            ubicacion=telefono['ubicacion'], 
            telefono=telefono['telefono'], 
            num_telefono=telefono['num_telefono'], 
            estado=telefono['estado'], 
            informacion=telefono['informacion']
        )

        db.add(new_telefono)
        db.commit()
        db.refresh(new_telefono)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'error creando usuario {e}')


def update(id: int, telefono: Fono, db: Session):
    telefonodb = get_by_id(id, db)

    telefonodb.nivel = telefono.nivel
    telefonodb.ubicacion = telefono.ubicacion
    telefonodb.telefono = telefono.telefono
    telefonodb.num_telefono = telefono.num_telefono
    telefonodb.estado = telefono.estado
    telefonodb.informacion = telefono.informacion

    db.add(telefonodb)
    db.commit()
    db.refresh(telefonodb)

    return telefonodb


def delete(id: int, db: Session):
    telefonodb = get_by_id(id, db)

    db.delete(telefonodb)
    db.commit()