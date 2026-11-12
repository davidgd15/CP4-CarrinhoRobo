
"""
Módulo de previsão ambiental do AviRonda.
"""

import joblib

from config.configuracoes import MODELO_PATH


def carregar_modelo():
    """Carrega o modelo treinado."""

    if not MODELO_PATH.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado: {MODELO_PATH}"
        )

    return joblib.load(MODELO_PATH)


def classificar_ambiente(modelo, temperatura, humidade):
    """Classifica as condições ambientais."""

    dados = [[temperatura, humidade]]

    resultado = modelo.predict(dados)[0]
    probabilidades = modelo.predict_proba(dados)[0]
    confianca = float(max(probabilidades)) * 100

    return {
        "classificacao": resultado,
        "confianca": round(confianca, 2)
    }
