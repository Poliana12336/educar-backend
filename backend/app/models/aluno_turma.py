from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class AlunoTurma(Base):

    __tablename__ = "aluno_turma"

    id = Column(Integer, primary_key=True, index=True)

    aluno_id = Column(Integer, ForeignKey("users.id"))

    turma_id = Column(Integer, ForeignKey("turmas.id"))