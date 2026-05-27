from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User
from app.models.turma import Turma
from app.models.capitulo import Capitulo
from app.models.liberacao import Liberacao
from app.models.aluno_turma import AlunoTurma

router = APIRouter()


# ==========================================
# CAPÍTULOS LIBERADOS DO ALUNO
# ==========================================

@router.get("/aluno/{aluno_id}/capitulos")

def capitulos_liberados(
    aluno_id: int,
    db: Session = Depends(get_db)
):

    # descobrir turma do aluno
    aluno_turma = db.query(AlunoTurma).filter(
        AlunoTurma.aluno_id == aluno_id
    ).first()

    if not aluno_turma:
        return []

    turma_id = aluno_turma.turma_id

    # buscar liberações
    liberacoes = db.query(Liberacao).filter(
        Liberacao.turma_id == turma_id,
        Liberacao.liberado == True
    ).all()

    capitulos = []

    for l in liberacoes:

        capitulo = db.query(Capitulo).filter(
            Capitulo.id == l.capitulo_id
        ).first()

        if capitulo:
            capitulos.append(capitulo)

    return capitulos