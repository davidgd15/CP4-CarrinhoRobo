"""
Módulo de registo das leituras ambientais do AviRonda.
"""

import csv
from datetime import datetime

from config.configuracoes import CSV_PATH


def registar_leitura(leitura, resultado):

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    ficheiro_existe = CSV_PATH.exists()

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as ficheiro:

        campos = [
            "data_hora",
            "temperatura",
            "humidade",
            "classificacao",
            "confianca",
            "origem"
        ]

        escritor = csv.DictWriter(
            ficheiro,
            fieldnames=campos
        )

        if not ficheiro_existe:
            escritor.writeheader()

        escritor.writerow({
            "data_hora": datetime.now().isoformat(timespec="seconds"),
            "temperatura": leitura["temperatura"],
            "humidade": leitura["humidade"],
            "classificacao": resultado["classificacao"],
            "confianca": resultado["confianca"],
            "origem": leitura["origem"]
        })

    print("Leitura registada no histórico CSV.")
    