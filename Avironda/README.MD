# AviRonda – Monitorização Ambiental Inteligente para Aviários

## 1. Descrição do Projeto

O AviRonda é um projeto de robótica desenvolvido no âmbito do FIAP, com o objetivo de apoiar a monitorização das condições ambientais em aviários.

A solução utiliza um Raspberry Pi para processar informações de temperatura e humidade, aplicar um modelo de Inteligência Artificial e apresentar uma classificação do ambiente.

## 2. Objetivos

- Monitorizar temperatura e humidade.
- Processar dados ambientais através de um modelo de Machine Learning.
- Classificar as condições como ADEQUADO ou ALERTA.
- Sinalizar o estado através de LEDs.
- Registar o histórico de leituras num ficheiro CSV.

## 3. Arquitetura

O fluxo de funcionamento previsto é:

1. Obtenção dos dados ambientais.
2. Processamento dos valores no Raspberry Pi.
3. Classificação através do modelo de Inteligência Artificial.
4. Identificação do estado ambiental.
5. Sinalização através dos LEDs.
6. Registo do histórico em CSV.

## 4. Tecnologias Utilizadas

- Python
- Raspberry Pi
- NumPy
- Scikit-learn
- Random Forest
- Joblib
- CSV
- GPIO Zero

## 5. Inteligência Artificial

O projeto utiliza um modelo Random Forest Classifier para classificar condições de temperatura e humidade.

O modelo foi treinado com um conjunto de dados gerados para desenvolvimento, utilizando regras de classificação provisórias.

A avaliação inicial apresentou uma acurácia de aproximadamente 99,95% nesse conjunto de teste sintético. Este resultado não representa uma validação em condições reais de aviários.

## 6. Sinalização Visual

O sistema prevê dois indicadores:

- LED verde: ambiente classificado como ADEQUADO.
- LED vermelho: ambiente classificado como ALERTA.

## 7. Registo de Dados

As informações são guardadas em `logs/leituras_avironda.csv`, incluindo:

- Data e hora.
- Temperatura.
- Humidade.
- Classificação.
- Confiança do modelo.
- Origem dos dados.

## 8. Estado do Desenvolvimento

- [x] Estrutura inicial do projeto.
- [x] Fonte de dados para testes.
- [x] Treinamento do modelo de IA.
- [x] Módulo de previsão.
- [x] Registo histórico CSV.
- [x] Módulo de controlo dos LEDs.
- [ ] Validação do sensor DHT11.
- [ ] Testes integrados no Raspberry Pi.
- [ ] Demonstração física completa.

## 9. Limitações

A classificação depende dos limites ambientais configurados no sistema. Estes limites são provisórios e necessitam de validação adequada antes de uma utilização em aviários reais.

O sensor DHT11 ainda necessita de validação física. Os dados gerados para desenvolvimento não devem ser interpretados como medições reais.

## 10. Objetivo Final

Desenvolver um sistema robótico capaz de apoiar a monitorização ambiental em aviários, combinando robótica, sensores, processamento de dados e Inteligência Artificial.