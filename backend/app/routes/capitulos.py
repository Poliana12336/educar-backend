from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.capitulo import Capitulo
from app.models.liberacao import Liberacao

router = APIRouter()


# ==================================
# LISTAR CAPÍTULOS
# ==================================

@router.get("/capitulos")

def listar_capitulos(db: Session = Depends(get_db)):

    return db.query(Capitulo).all()


# ==================================
# LIBERAR CAPÍTULO
# ==================================

@router.post("/liberar")

def liberar_capitulo(
    professor_id: int,
    turma_id: int,
    capitulo_id: int,
    db: Session = Depends(get_db)
):

    liberacao = Liberacao(
        professor_id=professor_id,
        turma_id=turma_id,
        capitulo_id=capitulo_id,
        liberado=True
    )

    db.add(liberacao)
    db.commit()

    return {"message": "Capítulo liberado"}

# ==================================
# OBTER CAPÍTULO ESPECÍFICO
# ==================================

@router.get("/capitulo/{capitulo_id}")

def obter_capitulo(
    capitulo_id: int,
    db: Session = Depends(get_db)
):

    capitulo = db.query(Capitulo).filter(
        Capitulo.id == capitulo_id
    ).first()

    if not capitulo:
        return {"erro": "Capítulo não encontrado"}

    return capitulo