from app.database import SessionLocal
from app.models.capitulo import Capitulo

from app.seeds.capitulos_seed import CAPITULOS


db = SessionLocal()

for c in CAPITULOS:

    existe = db.query(Capitulo).filter(
        Capitulo.numero == c["numero"]
    ).first()

    if not existe:

        capitulo = Capitulo(
            numero=c["numero"],
            titulo=c["titulo"],
            disciplina=c["disciplina"],
            resumo=c["resumo"],
            marker=c["marker"],
            modulo_ar=c["modulo_ar"]
        )

        db.add(capitulo)

db.commit()

print("Seed executada com sucesso!")