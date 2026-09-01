#Entrada de dados
nome_aparelho = input("Qual o nome do aparelho? ") 
potencia_w= float(input("Qual a potência do aparelho em Watts(W)?"))
horas_diarias= float(input("Qual o tempo médio em horas por dia?"))
# Processamento de dados
consumo_mensal_kwh= (potencia_w * horas_diarias * 30)/1000
custo_estimado= consumo_mensal_kwh * 0.78938
# Saída de dados
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal_kwh} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")