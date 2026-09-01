# 🧮 Calculadora de Consumo Elétrico

## Sobre o projeto

Calculadora para calcular o consumo elétrico de eletrodomésticos de acordo com suas horas de uso, além de fornecer uma estimativa do consumo de energia e do custo em reais.

## Linguagem utilizada

Python

## Fórmulas utilizadas

### Consumo mensal

`consumo_mensal_kwh = (potencia_w * horas_diarias * 30) / 1000`

### Custo estimado

`custo_estimado = consumo_mensal_kwh * 0.78938`

> **Observação:** Para a estimativa de custo, foi utilizada como referência a tarifa-base residencial do estado de São Paulo, no valor de R$ 0,78938 por kWh. O valor apresentado pelo programa é apenas uma estimativa e pode variar de acordo com impostos, bandeiras tarifárias e outros componentes da conta de energia.

## Como informar as horas de uso

O tempo de uso do aparelho deve ser informado em **horas**. Caso o aparelho seja utilizado por horas e minutos, utilize a conversão abaixo:

| Minutos | Valor em horas |
|---------|----------------|
| 10 min | 0.17 |
| 20 min | 0.33 |
| 30 min | 0.50 |
| 40 min | 0.67 |
| 50 min | 0.83 |
| 60 min | 1.00 |

### Exemplos

- 30 minutos → `0.50`
- 1 hora → `1`
- 1 hora e 30 minutos → `1.50`
- 1 hora e 40 minutos → `1.67`
- 2 horas e 20 minutos → `2.33`
- 8 horas → `8`
- 24 horas → `24`

> **Importante:** Para valores decimais, utilize ponto (`.`) em vez de vírgula (`,`).

## Como utilizar

1. Execute o arquivo `app.py`.
2. Digite o nome do eletrodoméstico e pressione **Enter**.
3. Digite a potência do aparelho em Watts (W) e pressione **Enter**.
4. Digite o tempo médio de uso do aparelho em horas por dia.
5. Pressione **Enter** e o programa apresentará o consumo mensal estimado em kWh e o custo estimado em reais.

## Tecnologias e recursos

<img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" height="20">
<img src="https://img.shields.io/badge/GitHub-Repositório-black?logo=github&logoColor=white" height="20">
<img src="https://img.shields.io/badge/⚡-Energia-yellow" height="20">
