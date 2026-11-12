

"""
Treinamento do modelo de Inteligência Artificial AviRonda.

O modelo utiliza dados ambientais gerados para aprender
a classificar condições de temperatura e humidade.

Algoritmo: Random Forest Classifier.
"""

import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from config.configuracoes import (
    TEMP_MIN,
    TEMP_MAX,
    HUM_MIN,
    HUM_MAX,
    MODELO_PATH
)


def gerar_dataset(total=10000):
    """Cria dados ambientais para treinamento."""

    np.random.seed(42)

    temperaturas = np.random.uniform(10, 40, total)
    humidades = np.random.uniform(20, 95, total)

    X = np.column_stack((temperaturas, humidades))

    y = np.where(
        (temperaturas >= TEMP_MIN) &
        (temperaturas <= TEMP_MAX) &
        (humidades >= HUM_MIN) &
        (humidades <= HUM_MAX),
        "ADEQUADO",
        "ALERTA"
    )

    return X, y


def treinar_modelo():
    """Treina, avalia e guarda o modelo."""

    print("AVIRONDA - TREINAMENTO DA IA")
    print("--------------------------------")

    X, y = gerar_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    modelo = RandomForestClassifier(
        n_estimators=150,
        max_depth=12,
        random_state=42,
        class_weight="balanced"
    )

    print("Treinando modelo Random Forest...")

    modelo.fit(X_train, y_train)

    previsoes = modelo.predict(X_test)

    acuracia = accuracy_score(y_test, previsoes)

    print("\nResultados da avaliação:")
    print(f"Acurácia: {acuracia:.2%}")
    print("\nRelatório de classificação:")
    print(classification_report(y_test, previsoes))

    MODELO_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(modelo, MODELO_PATH)

    print(f"\nModelo guardado em: {MODELO_PATH}")
    print("Treinamento concluído!")


if __name__ == "__main__":
    treinar_modelo()
