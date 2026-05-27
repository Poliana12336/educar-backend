from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app.database import Base

class Progresso(Base):

    __tablename__ = "progresso"

    id = Column(Integer, primary_key=True, index=True)

    aluno_id = Column(Integer, ForeignKey("users.id"))

    capitulo_id = Column(Integer, ForeignKey("capitulos.id"))

    concluido = Column(Boolean, default=False)