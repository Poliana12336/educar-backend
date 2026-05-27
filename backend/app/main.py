from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base

# models
from app.models.user import User
from app.models.turma import Turma
from app.models.aluno_turma import AlunoTurma
from app.models.capitulo import Capitulo
from app.models.liberacao import Liberacao
from app.models.progresso import Progresso

# rotas
from app.routes.users import router as users_router
from app.routes.turmas import router as turmas_router
from app.routes.capitulos import router as capitulos_router
from app.routes.progresso import router as progresso_router
from app.routes.aluno import router as aluno_router
from app.routes.aluno_turma import router as aluno_turma_router

# criar banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# registrar rotas
app.include_router(users_router)
app.include_router(turmas_router)
app.include_router(capitulos_router)
app.include_router(progresso_router)
app.include_router(aluno_router)
app.include_router(aluno_turma_router)


@app.get("/")
def raiz():
    return {"message": "educAR API online"}