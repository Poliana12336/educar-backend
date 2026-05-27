from sqlalchemy import Column, Integer, String
from app.database import Base

class Turma(Base):

    __tablename__ = "turmas"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)