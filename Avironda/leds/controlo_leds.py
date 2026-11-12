"""
Controlo dos LEDs de estado do AviRonda.

LED verde: ambiente ADEQUADO.
LED vermelho: ambiente em ALERTA.
"""

from config.configuracoes import (
    GPIO_LED_VERDE,
    GPIO_LED_VERMELHO
)


class ControloLEDs:

    def __init__(self):

        self.gpio = None
        self.led_verde = None
        self.led_vermelho = None

    def iniciar(self):

        try:
            from gpiozero import LED

            self.led_verde = LED(GPIO_LED_VERDE)
            self.led_vermelho = LED(GPIO_LED_VERMELHO)

            self.gpio = True

            print("LEDs inicializados com sucesso.")

        except Exception as erro:

            self.gpio = False

            print(f"Não foi possível inicializar os LEDs: {erro}")

    def atualizar(self, classificacao):

        if not self.gpio:
            print("Controlo físico dos LEDs indisponível.")
            return

        if classificacao == "ADEQUADO":

            self.led_verde.on()
            self.led_vermelho.off()

        else:

            self.led_verde.off()
            self.led_vermelho.on()

    def desligar(self):

        if self.gpio:

            self.led_verde.off()
            self.led_vermelho.off()

            self.led_verde.close()
            self.led_vermelho.close()

            print("LEDs desligados.")