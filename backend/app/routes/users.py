from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

router = APIRouter()


# =========================
# CADASTRAR USUÁRIO
# =========================

@router.post("/users")

def criar_usuario(
    nome: str,
    email: str,
    senha: str,
    role: str,
    db: Session = Depends(get_db)
):

    usuario = User(
        nome=nome,
        email=email,
        senha=senha,
        role=role
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


# =========================
# LISTAR USUÁRIOS
# =========================

@router.get("/users")

def listar_usuarios(db: Session = Depends(get_db)):

    usuarios = db.query(User).all()

    return usuarios


# =========================
# LOGIN
# =========================

@router.post("/login")

def login(
    email: str,
    senha: str,
    db: Session = Depends(get_db)
):

    usuario = db.query(User).filter(
        User.email == email,
        User.senha == senha
    ).first()

    if not usuario:
        return {"erro": "Usuário inválido"}

    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "role": usuario.role
    }