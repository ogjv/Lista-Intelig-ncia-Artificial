# Importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Criar um gráfico para Macaé
plt.figure(figsize=(10, 6))  # Define o tamanho da figura

# Lê os dados de Macaé de um arquivo CSV usando Pandas
macae_df = pd.read_csv('c:/Users/jvama/ListaIA/Q3/dados_climaticos.txt', encoding='ISO-8859-1')

# Lê os dados do Rio de Janeiro de um arquivo CSV usando Pandas
rio_df = pd.read_csv('c:/Users/jvama/ListaIA/Q3/temperaturas_rio.txt', encoding='ISO-8859-1')

# Plotar as curvas de temperatura para Macaé
plt.plot(range(1, 13), macae_df['Tmin'], marker='o', label='Macaé - Tmin')  # Temperatura mínima
plt.plot(range(1, 13), macae_df['Tmax'], marker='o', label='Macaé - Tmax')  # Temperatura máxima
plt.plot(range(1, 13), macae_df['Tmedia'], marker='o', label='Macaé - Tmedia')  # Temperatura média

# Configurar rótulos e título do gráfico de Macaé
plt.xlabel('Mês')  # Rótulo do eixo X
plt.ylabel('Temperatura (°C)')  # Rótulo do eixo Y
plt.title('Temperaturas em Macaé ao longo do ano')  # Título do gráfico
plt.legend()  # Mostrar a legenda
plt.grid(True)  # Habilitar as linhas de grade

# Salvar o gráfico de Macaé como uma figura
plt.savefig('macae_temperaturas.png')  # Salva a figura em um arquivo
plt.close()  # Fecha o gráfico

# Repetir o processo para o Rio de Janeiro
plt.figure(figsize=(10, 6))  # Define o tamanho da figura

# Plotar as curvas de temperatura para o Rio de Janeiro
plt.plot(range(1, 13), rio_df['Tmin'], marker='o', label='Rio de Janeiro - Tmin')  # Temperatura mínima
plt.plot(range(1, 13), rio_df['Tmax'], marker='o', label='Rio de Janeiro - Tmax')  # Temperatura máxima
plt.plot(range(1, 13), rio_df['Tmedia'], marker='o', label='Rio de Janeiro - Tmedia')  # Temperatura média

# Configurar rótulos e título do gráfico do Rio de Janeiro
plt.xlabel('Mês')  # Rótulo do eixo X
plt.ylabel('Temperatura (°C)')  # Rótulo do eixo Y
plt.title('Temperaturas no Rio de Janeiro ao longo do ano')  # Título do gráfico
plt.legend()  # Mostrar a legenda
plt.grid(True)  # Habilitar as linhas de grade

# Salvar o gráfico do Rio de Janeiro como uma figura
plt.savefig('rio_temperaturas.png')  # Salva a figura em um arquivo
plt.close()  # Fecha o gráfico
