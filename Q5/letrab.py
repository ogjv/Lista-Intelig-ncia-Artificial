import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Suponhamos que você já tenha lido os dados em DataFrames para Macaé e Rio de Janeiro
# macae_df e rio_df são os DataFrames correspondentes

# Criar um gráfico de barras agrupado
months = range(1, 13)
bar_width = 0.35
index = np.arange(len(months))

plt.figure(figsize=(10, 6))
plt.bar(index - bar_width/2, macae_df['Tmedia'], bar_width, label='Macaé', color='b', alpha=0.7)
plt.bar(index + bar_width/2, rio_df['Tmedia'], bar_width, label='Rio de Janeiro', color='g', alpha=0.7)
plt.xlabel('Mês')
plt.ylabel('Temperatura Média (°C)')
plt.title('Comparação das Temperaturas Médias entre Macaé e Rio de Janeiro')
plt.xticks(index, months)
plt.legend()
plt.grid(True)

# Salvar o gráfico de barras
plt.savefig('comparacao_temperaturas.png')
plt.close()
