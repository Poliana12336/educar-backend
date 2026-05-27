from app.database import Base, engine

# IMPORTAR TODOS OS MODELS
from app.models.capitulo import Capitulo

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")