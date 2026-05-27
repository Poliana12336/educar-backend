from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.progresso import Progresso

router = APIRouter()


# ==================================
# CONCLUIR CAPÍTULO
# ==================================

@router.post("/progresso")

def concluir_capitulo(
    aluno_id: int,
    capitulo_id: int,
    db: Session = Depends(get_db)
):

    existente = db.query(Progresso).filter(
        Progresso.aluno_id == aluno_id,
        Progresso.capitulo_id == capitulo_id
    ).first()

    if existente:
        return {"message": "Já concluído"}

    progresso = Progresso(
        aluno_id=aluno_id,
        capitulo_id=capitulo_id,
        concluido=True
    )

    db.add(progresso)
    db.commit()

    return {"message": "Capítulo concluído"}