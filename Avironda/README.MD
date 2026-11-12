# AviRonda – Monitorização Ambiental Inteligente para Aviários

## 1. Descrição do Projeto

O **AviRonda** é um projeto de robótica desenvolvido no âmbito da FIAP, com o objetivo de apoiar a monitorização ambiental em aviários através da integração de sensores, robótica e Inteligência Artificial.

A solução utiliza um Raspberry Pi para obter e processar informações de temperatura e humidade, aplicar um modelo de Machine Learning e classificar as condições ambientais.

A partir dessa classificação, o sistema pode sinalizar o estado do ambiente através de LEDs e armazenar o histórico das informações recolhidas.

## 2. Objetivos

- Monitorizar as condições de temperatura e humidade.
- Processar dados ambientais através de Inteligência Artificial.
- Classificar as condições como ADEQUADO ou ALERTA.
- Sinalizar visualmente as condições identificadas.
- Armazenar o histórico de leituras num ficheiro CSV.
- Demonstrar a aplicação da robótica e da IA no apoio à monitorização ambiental.

## 3. Arquitetura do Sistema

O funcionamento do AviRonda está organizado no seguinte fluxo:

1. Obtenção dos dados de temperatura e humidade.
2. Envio das informações para processamento no Raspberry Pi.
3. Análise dos valores pelo modelo de Inteligência Artificial.
4. Classificação das condições ambientais.
5. Sinalização do resultado através dos LEDs.
6. Registo das informações num histórico CSV.

A arquitetura foi organizada em módulos independentes para facilitar a manutenção e a evolução do projeto.

## 4. Tecnologias Utilizadas

- Python
- Raspberry Pi
- DHT11
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

A avaliação inicial apresentou aproximadamente 99,95% de acurácia num conjunto de teste sintético.

Esse resultado demonstra o funcionamento do modelo dentro das regras utilizadas no treinamento, não representando uma validação científica ou uma garantia de desempenho em aviários reais.

## 6. Monitorização Ambiental e Sinalização Visual

O sistema foi estruturado para trabalhar com um sensor DHT11, responsável pela obtenção de informações de temperatura e humidade.

A classificação produzida pela Inteligência Artificial é associada a dois indicadores visuais:

- **LED verde:** ambiente classificado como ADEQUADO.
- **LED vermelho:** ambiente classificado como ALERTA.

Quando não é possível utilizar o sensor físico, o sistema dispõe de uma fonte de dados gerados por software para permitir a demonstração e os testes da lógica de processamento.

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

A identificação da origem permite distinguir os dados gerados por software das futuras medições obtidas através do sensor físico.

## 8. Organização do Projeto

O código foi dividido em módulos independentes, organizados por responsabilidade:

```text
Avironda/
├── ai/
│   ├── modelo_avironda.pkl
│   ├── predict.py
│   ├── train_model.py
│   └── test_model.py
├── config/
│   └── configuracoes.py
├── leds/
│   └── controlo_leds.py
├── logs/
│   ├── leituras_avironda.csv
│   └── registar_leitura.py
├── sensores/
│   └── fonte_dados.py
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

Os testes confirmaram o funcionamento integrado dos módulos de geração de dados, previsão e armazenamento.

O controlo físico dos LEDs e a integração completa com o Raspberry Pi são etapas de validação no hardware.

## 11. Limitações e Considerações

Os limites ambientais utilizados para a classificação são provisórios e necessitam de validação técnica de acordo com as características do aviário, a espécie e a idade das aves.

O sensor DHT11 necessita de validação física para confirmar a fiabilidade das leituras.

Os dados gerados por software são utilizados exclusivamente para desenvolvimento e demonstração, não devendo ser interpretados como medições reais do ambiente.

A confiança apresentada pelo modelo corresponde à estimativa produzida pelo classificador e não representa uma garantia de exatidão.

## 12. Objetivo Final

O objetivo do AviRonda é demonstrar como a integração entre robótica, sensores, processamento de dados e Inteligência Artificial pode contribuir para a monitorização ambiental em aviários.

A proposta procura desenvolver uma solução modular, acessível e expansível, capaz de identificar condições ambientais que mereçam atenção e apoiar a tomada de decisões através de sinalização visual e registo histórico.