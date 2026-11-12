
"""
Configurações centrais do projeto AviRonda.
"""

from pathlib import Path

# Diretório principal do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Modos de funcionamento
MODO_REAL = "REAL"
MODO_DEMONSTRACAO = "DEMONSTRACAO"

# Modo utilizado inicialmente
MODO_ATUAL = MODO_DEMONSTRACAO

# GPIO - numeração BCM do Raspberry Pi
GPIO_DHT11 = 12
GPIO_LED_VERMELHO = 26
GPIO_LED_VERDE = 19

# Intervalo entre leituras (segundos)
INTERVALO_LEITURA = 5

# Limites provisórios para demonstração.
# Devem ser validados antes de utilização em aviários reais.
TEMP_MIN = 20
TEMP_MAX = 30
HUM_MIN = 40
HUM_MAX = 75

# Caminhos dos ficheiros
MODELO_PATH = BASE_DIR / "ai" / "modelo_avironda.pkl"
LOGS_DIR = BASE_DIR / "logs"
CSV_PATH = LOGS_DIR / "leituras_avironda.csv"

# Criar diretório de logs caso não exista
LOGS_DIR.mkdir(parents=True, exist_ok=True)
