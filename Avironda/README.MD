# AviRonda – Monitorização Ambiental Inteligente para Aviários

## 1. Descrição do Projeto

link video do projeto: https://www.youtube.com/watch?v=HAiARoLpH-0

O **AviRonda** é um projeto de robótica desenvolvido no âmbito da FIAP, com o objetivo de apoiar a monitorização ambiental em aviários através da integração de sensores, robótica e Inteligência Artificial.

A solução utiliza um Raspberry Pi e um sensor DHT11 para obter informações de temperatura e humidade, processar os dados através de um modelo de Machine Learning e classificar as condições ambientais.

A partir dessa classificação, o sistema sinaliza o estado do ambiente através de LEDs e armazena o histórico das informações recolhidas.

O projeto possui uma arquitetura modular, permitindo a expansão de funcionalidades e a utilização de dados simulados para testes e demonstrações.

## 2. Objetivos

- Monitorizar as condições de temperatura e humidade.
- Obter informações ambientais através do sensor DHT11.
- Processar dados ambientais através de Inteligência Artificial.
- Classificar as condições como ADEQUADO ou ALERTA.
- Sinalizar visualmente as condições identificadas.
- Armazenar o histórico de leituras num ficheiro CSV.
- Executar ciclos de monitorização de forma automática.
- Demonstrar a aplicação da robótica e da IA no apoio à monitorização ambiental.

## 3. Arquitetura do Sistema

O funcionamento do AviRonda está organizado no seguinte fluxo:

1. Obtenção dos dados de temperatura e humidade através do DHT11.
2. Envio das informações para processamento no Raspberry Pi.
3. Análise dos valores pelo modelo de Inteligência Artificial.
4. Classificação das condições ambientais.
5. Sinalização do resultado através dos LEDs.
6. Registo das informações num histórico CSV.
7. Repetição automática do processo após o intervalo configurado.

A arquitetura foi organizada em módulos independentes para facilitar a manutenção e a evolução do projeto.

## 4. Tecnologias Utilizadas

- Python
- Raspberry Pi
- Sensor DHT11
- NumPy
- Scikit-learn
- Random Forest Classifier
- Joblib
- CSV
- GPIO Zero
- Visual Studio Code
- Git e GitHub

## 5. Inteligência Artificial

O AviRonda utiliza um modelo **Random Forest Classifier**, desenvolvido com Scikit-learn, para analisar os valores de temperatura e humidade.

O modelo foi treinado com dados sintéticos, utilizando limites ambientais provisórios para definir duas categorias:

- **ADEQUADO:** valores dentro dos intervalos configurados.
- **ALERTA:** valores fora dos intervalos configurados.

Os limites utilizados inicialmente são:

- Temperatura: 20 °C a 30 °C.
- Humidade: 40% a 75%.

A avaliação inicial apresentou aproximadamente 99,95% de acurácia num conjunto de teste sintético.

Esse resultado demonstra o funcionamento do modelo dentro das regras utilizadas no treinamento, não representando uma validação científica ou uma garantia de desempenho em aviários reais.

O módulo `predict.py` é responsável por carregar o modelo treinado, realizar as previsões e apresentar a confiança estimada pelo classificador.

## 6. Monitorização Ambiental e Sinalização Visual

O AviRonda utiliza o sensor DHT11 como componente de aquisição de dados ambientais, permitindo obter informações de temperatura e humidade.

A classificação produzida pela Inteligência Artificial é associada a dois indicadores visuais:

- **LED verde:** ambiente classificado como ADEQUADO.
- **LED vermelho:** ambiente classificado como ALERTA.

O sistema também possui uma fonte de dados gerados por software, utilizada para testes e demonstrações do processamento e da classificação realizados pela IA.

### Monitorização automática

O ficheiro `main.py` coordena o funcionamento contínuo do AviRonda.

O programa executa as seguintes operações:

1. Obtém os dados ambientais.
2. Envia os valores para o modelo de IA.
3. Recebe a classificação do ambiente.
4. Atualiza os LEDs de acordo com o resultado.
5. Regista as informações no histórico CSV.
6. Aguarda o intervalo configurado e inicia um novo ciclo.

O intervalo de monitorização está definido inicialmente em 5 segundos, podendo ser alterado no ficheiro `config/configuracoes.py`.

No modo de demonstração, o programa utiliza dados gerados por software, identificados como `DADOS_GERADOS`.

## 7. Registo e Histórico de Dados

O AviRonda possui um módulo responsável pelo armazenamento das informações num ficheiro CSV localizado em:

`logs/leituras_avironda.csv`

Cada registo contém:

- Data e hora da leitura.
- Temperatura.
- Humidade.
- Classificação ambiental.
- Confiança indicada pelo modelo.
- Origem dos dados.

A identificação da origem permite distinguir os dados gerados por software das medições obtidas através do sensor físico.

O histórico permite acompanhar as classificações realizadas pelo sistema ao longo do tempo.

## 8. Organização do Projeto

O código foi dividido em módulos independentes, organizados por responsabilidade:

```text
Avironda/
├── ai/
│   ├── __init__.py
│   ├── modelo_avironda.pkl
│   ├── predict.py
│   ├── train_model.py
│   └── test_model.py
├── config/
│   ├── __init__.py
│   └── configuracoes.py
├── leds/
│   ├── __init__.py
│   └── controlo_leds.py
├── logs/
│   ├── .gitkeep
│   ├── leituras_avironda.csv
│   └── registar_leitura.py
├── sensores/
│   ├── __init__.py
│   └── fonte_dados.py
├── main.py
├── README.MD
└── .gitignore
```

Essa organização separa a inteligência artificial, a configuração, o controlo dos LEDs, a gestão dos dados e os módulos relacionados com os sensores.

## 9. Integração com o Carrinho Robótico

O AviRonda foi desenvolvido dentro do repositório original do carrinho robótico, como um módulo independente.

A implementação mantém separação em relação aos códigos originais dos projetos CP1 e CP2, preservando os módulos responsáveis pela movimentação do carrinho e pela deteção de movimento.

Essa abordagem permite acrescentar novas funcionalidades sem comprometer os recursos já desenvolvidos.

## 10. Testes e Validação

Foram realizados testes de software no ambiente Windows, com resultados que demonstraram:

- Geração de valores simulados de temperatura e humidade.
- Processamento dos dados pelo modelo de Inteligência Artificial.
- Classificação dos ambientes como ADEQUADO ou ALERTA.
- Apresentação da confiança indicada pelo modelo.
- Registo automático das informações no histórico CSV.
- Verificação da sintaxe dos módulos Python.

O modelo de IA também foi carregado e executado com sucesso no Raspberry Pi, utilizando o modelo disponível no equipamento.

O funcionamento contínuo de todos os módulos em conjunto e a integração física dos LEDs devem ser validados no hardware.

## 11. Limitações e Considerações

Os limites ambientais utilizados para a classificação são provisórios e necessitam de validação técnica de acordo com as características do aviário, a espécie e a idade das aves.

Os dados gerados por software são utilizados para desenvolvimento, testes e demonstrações, não devendo ser interpretados como medições reais do ambiente.

A confiança apresentada pelo modelo corresponde à estimativa produzida pelo classificador e não representa uma garantia de exatidão.

O DHT11 mede temperatura e humidade, não sendo capaz de identificar diretamente gases como amónia ou dióxido de carbono.

## 12. Objetivo Final

O objetivo do AviRonda é demonstrar como a integração entre robótica, sensores, processamento de dados e Inteligência Artificial pode contribuir para a monitorização ambiental em aviários.

A proposta procura desenvolver uma solução modular, acessível e expansível, capaz de identificar condições ambientais que mereçam atenção e apoiar a tomada de decisões através de sinalização visual e registo histórico.
