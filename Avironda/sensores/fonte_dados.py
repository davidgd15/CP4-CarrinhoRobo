
"""
Módulo de fornecimento de dados ambientais do AviRonda.

No ambiente de desenvolvimento, o sensor pode não apresentar
variações reais de temperatura e humidade suficientes para
validar o modelo de IA.

Por isso, este módulo permite gerar valores dentro de intervalos
plausíveis para testar o processamento e a classificação.
"""

import random


def gerar_leitura():
    """
    Gera valores ambientais para testes do sistema.
    """

    temperatura = round(random.uniform(15.0, 38.0), 1)
    humidade = round(random.uniform(30.0, 90.0), 1)

    return {
        "temperatura": temperatura,
        "humidade": humidade,
        "origem": "DADOS_GERADOS"
    }


if __name__ == "__main__":

    print("AVIRONDA - FONTE DE DADOS AMBIENTAIS")
    print("------------------------------------")

    for numero in range(5):

        leitura = gerar_leitura()

        print(f"\nLeitura {numero + 1}")
        print(f"Temperatura: {leitura['temperatura']} °C")
        print(f"Humidade: {leitura['humidade']}%")
        print(f"Origem: {leitura['origem']}")
