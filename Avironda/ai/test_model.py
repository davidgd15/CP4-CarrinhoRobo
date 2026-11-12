"""
Teste de integração da IA, histórico CSV e LEDs do AviRonda.
"""

from ai.predict import carregar_modelo, classificar_ambiente
from sensores.fonte_dados import gerar_leitura
from logs.registar_leitura import registar_leitura
from leds.controlo_leds import ControloLEDs


def executar_teste():

    print("AVIRONDA - TESTE DE INTEGRACAO")
    print("--------------------------------")

    modelo = carregar_modelo()

    leds = ControloLEDs()

    leds.iniciar()

    try:

        for numero in range(5):

            leitura = gerar_leitura()

            resultado = classificar_ambiente(
                modelo,
                leitura["temperatura"],
                leitura["humidade"]
            )

            registar_leitura(leitura, resultado)

            leds.atualizar(resultado["classificacao"])

            print(f"\nLeitura {numero + 1}")
            print(f"Temperatura: {leitura['temperatura']} °C")
            print(f"Humidade: {leitura['humidade']}%")
            print(f"Classificação: {resultado['classificacao']}")
            print(f"Confiança: {resultado['confianca']}%")

    finally:

        leds.desligar()

    print("\nTeste concluído!")


if __name__ == "__main__":
    executar_teste()