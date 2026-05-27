from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Capitulo(Base):

    __tablename__ = "capitulos"

    id = Column(Integer, primary_key=True, index=True)

    numero = Column(Integer)

    titulo = Column(String)

    disciplina = Column(String)

    resumo = Column(Text)

    marker = Column(String)

    modulo_ar = Column(String)