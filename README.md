# Documentação Técnica — Chassi do Robô Arduino

## Equipe

| Integrante | RM |
|---|---|
| David Denunci | RM98603 |
| Fernando Popolili | RM99919 |
| Lucas de Toledo | RM97913 |
| Matheus Zanardi | RM98832 |
| Augusto Milreu | RM98245 |

---

## 1. Ficha de Requisitos

### 1.1 Dimensões gerais do chassi

| Parâmetro | Valor |
|---|---|
| Comprimento total | 180 mm |
| Largura total | 120 mm |
| Espessura da placa principal | 4 mm |
| Raio dos cantos arredondados | 10 mm |
| Material sugerido | Chapa rígida (acrílico/MDF/impressão 3D) |
| Simetria | Ao longo da linha de centro longitudinal |

### 1.2 Quantidade e tipo de motores

| Parâmetro | Valor |
|---|---|
| Quantidade de motores DC | 2 (um de cada lado, simétricos) |
| Tipo | Motor DC com caixa de redução (gearbox) |
| Diâmetro da roda | ~65 mm |
| Largura da roda | ~25 mm |
| Altura do eixo em relação à base | ~35 mm |
| Apoio auxiliar | Roda castor (ball caster) centralizada, eixo longitudinal |

### 1.3 Placa controladora

| Parâmetro | Valor |
|---|---|
| Placa | Arduino Uno |
| Dimensões aproximadas | 68,6 mm × 53,4 mm |
| Posição | Centro da região superior do chassi |
| Furos de fixação | 4 furos, Ø 3,2 mm |
| Observações | Espaço livre reservado para conectores USB e alimentação |

### 1.4 Posição dos componentes

| Componente | Posição no chassi |
|---|---|
| Arduino Uno | Centro superior |
| Suporte de bateria (4×AA) | Traseira, centralizado |
| Motores DC | Laterais, simétricos, região central/traseira |
| Rodas | Laterais, alinhadas ao eixo dos motores |
| Roda castor (caster) | Frente (ou traseira), centralizada no eixo longitudinal |
| Furos de passagem de cabos | Próximos ao Arduino e ao suporte de bateria |
| Furos de ventilação/alívio de peso | Áreas sem função estrutural, distribuídos pela placa |
| Furos de fixação de parafusos | Perímetro do chassi |

### 1.5 Suporte de bateria

| Parâmetro | Valor |
|---|---|
| Tipo | Suporte para 4 pilhas AA |
| Dimensões aproximadas | 65 mm × 60 mm × 18 mm |
| Posição | Região traseira do chassi |
| Fixação | Furos/slots de fixação + espaço para fio e conector |

### 1.6 Carenagem (cobertura)

| Parâmetro | Descrição |
|---|---|
| Função | Proteger componentes eletrônicos (Arduino, fiação, bateria) contra poeira e impactos leves |
| Fixação | Encaixe sobre os furos de parafuso do perímetro do chassi, ou suportes tipo coluna (standoffs) |
| Material sugerido | Mesmo material do chassi ou acrílico transparente para inspeção visual |
| Observação | Deve permitir acesso à porta USB e ao conector de alimentação sem remoção total da cobertura |

---

## 2. Croqui do Chassi

O croqui técnico (vistas superior, inferior, frontal, lateral e isométrica, com cotas em milímetros) foi desenvolvido como referência visual para fabricação, no padrão de desenho técnico/CAD. A ilustração com as cinco vistas e as anotações dimensionais está anexada como imagem de apoio a este documento (ver seção de anexos no repositório, pasta `/docs/croqui/`).

Principais cotas representadas no croqui:

- Comprimento total: 180 mm / Largura total: 120 mm
- Espessura da placa: 4 mm / Raio de canto: 10 mm
- Posição e furos de fixação do Arduino (Ø 3,2 mm)
- Área e furos do suporte de bateria (65 × 60 mm)
- Posição simétrica dos motores e diâmetro/largura das rodas (Ø 65 mm × 25 mm)
- Altura do eixo das rodas (35 mm da base)
- Posição da roda castor central
- Furos de passagem de cabos, ventilação e fixação de parafusos no perímetro

---
