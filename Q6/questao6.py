import pandas as pd
import numpy as np

# Ler o arquivo Excel
df = pd.read_excel("c:/Users/jvama/ListaIA/Q3/Dados_climaticos_historicos.xlsx", header=None)

# Definir o índice para a coluna de meses (por exemplo, a coluna 0)
df.set_index(0, inplace=True)

# Substituir valores não numéricos por NaN em todas as colunas numéricas
colunas_numericas = [1, 2, 3, 4, 5, 6, 7]
df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')

# Calcular a média anual para cada coluna numérica
media_anual = df[colunas_numericas].mean()

# Encontrar o mês com a maior e menor temperatura máxima
mes_max_temp = df[3].idxmax()
mes_min_temp = df[3].idxmin()

# Encontrar o mês mais chuvoso e menos chuvoso
mes_max_chuva = df[4].idxmax()
mes_min_chuva = df[4].idxmin()

# Calcular o acumulado de chuva anual
acumulado_chuva = df[4].sum()

# Determinar a cidade mais úmida com base no acumulado de chuva
cidade_mais_umida = "Macaé" if acumulado_chuva > 0 else "Rio de Janeiro"

# Exibir as estatísticas com os meses correspondentes
print("Média Anual:")
print(media_anual)

print("\nMês de Maior Temperatura Máxima:", mes_max_temp)
print("Mês de Menor Temperatura Mínima:", mes_min_temp)
print("Mês Mais Chuvoso:", mes_max_chuva)
print("Mês Menos Chuvoso:", mes_min_chuva)
print("Acumulado de Chuva Anual (mm):", acumulado_chuva)
print("Cidade Mais Úmida:", cidade_mais_umida)