
"""
AVIRONDA - Monitorização ambiental contínua.

Obtém dados ambientais, executa a IA,
controla os LEDs e regista o histórico.
"""

import time

from config.configuracoes import INTERVALO_LEITURA
from sensores.fonte_dados import gerar_leitura
from ai.predict import carregar_modelo, classificar_ambiente
from leds.controlo_leds import ControloLEDs
from logs.registar_leitura import registar_leitura


def main():

    print("=" * 45)
    print("AVIRONDA - MONITORIZACAO AMBIENTAL")
    print("=" * 45)
    print("Modo: DEMONSTRACAO (dados gerados)")
    print(f"Intervalo: {INTERVALO_LEITURA} segundos")

    # Carregar modelo de IA
    modelo = carregar_modelo()
    print("Modelo de IA carregado.")

    # Inicializar LEDs
    leds = ControloLEDs()
    leds.iniciar()

    numero_leitura = 0

    try:

        while True:

            numero_leitura += 1

            print("\n" + "-" * 45)
            print(f"LEITURA {numero_leitura}")

            # Obter dados ambientais simulados
            leitura = gerar_leitura()

            temperatura = leitura["temperatura"]
            humidade = leitura["humidade"]

            print(f"Temperatura: {temperatura} °C")
            print(f"Humidade: {humidade}%")
            print(f"Origem: {leitura['origem']}")

            # Classificar com Inteligência Artificial
            resultado = classificar_ambiente(
                modelo,
                temperatura,
                humidade
            )

            classificacao = resultado["classificacao"]

            print(f"Classificacao: {classificacao}")
            print(f"Confianca: {resultado['confianca']}%")

            # Atualizar LEDs
            leds.atualizar(classificacao)

            # Guardar histórico
            registar_leitura(leitura, resultado)

            print(
                f"Proxima verificacao em "
                f"{INTERVALO_LEITURA} segundos."
            )

            time.sleep(INTERVALO_LEITURA)

    except KeyboardInterrupt:

        print("\nMonitorizacao interrompida pelo utilizador.")

    finally:

        leds.desligar()
        print("AVIRONDA encerrado.")


if __name__ == "__main__":
    main()
