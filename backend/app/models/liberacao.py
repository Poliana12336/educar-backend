from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app.database import Base

class Liberacao(Base):

    __tablename__ = "liberacoes"

    id = Column(Integer, primary_key=True, index=True)

    professor_id = Column(Integer, ForeignKey("users.id"))

    turma_id = Column(Integer, ForeignKey("turmas.id"))

    capitulo_id = Column(Integer, ForeignKey("capitulos.id"))

    liberado = Column(Boolean, default=True)