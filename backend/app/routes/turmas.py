from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.turma import Turma

router = APIRouter()


# =========================
# CRIAR TURMA
# =========================

@router.post("/turmas")

def criar_turma(
    nome: str,
    db: Session = Depends(get_db)
):

    turma = Turma(nome=nome)

    db.add(turma)
    db.commit()
    db.refresh(turma)

    return turma


# =========================
# LISTAR TURMAS
# =========================

@router.get("/turmas")

def listar_turmas(db: Session = Depends(get_db)):

    turmas = db.query(Turma).all()

    return turmas