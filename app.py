# Calculadora de Consumo Elétrico
# Autor: Rayane Ferreira

# Entrada de dados
nome_aparelho = input("Digite o nome do aparelho: ") 
potencia_w= float(input("Digite a potência do aparelho em Watts(W): "))
horas_diarias= float(input("Digite o tempo médio em horas por dia: "))
# Processamento de dados
consumo_mensal_kwh= (potencia_w * horas_diarias * 30)/1000
custo_estimado= consumo_mensal_kwh * 0.78938
# Saída de dados
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal_kwh:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")
