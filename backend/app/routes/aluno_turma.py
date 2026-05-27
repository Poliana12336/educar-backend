from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db

from app.models.aluno_turma import AlunoTurma

router = APIRouter()


class AlunoTurmaCreate(BaseModel):
    aluno_id: int
    turma_id: int


@router.post("/aluno-turma")

def matricular_aluno(
    dados: AlunoTurmaCreate,
    db: Session = Depends(get_db)
):

    matricula = AlunoTurma(
        aluno_id=dados.aluno_id,
        turma_id=dados.turma_id
    )

    db.add(matricula)
    db.commit()
    db.refresh(matricula)

    return matricula