import pandas as pd
import matplotlib.pyplot as plt

# Criar um gráfico para Macaé
plt.figure(figsize=(10, 6))
macae_df = pd.read_csv('c:/Users/jvama/ListaIA/Q3/dados_climaticos.txt', encoding='ISO-8859-1')

rio_df = pd.read_csv('c:/Users/jvama/ListaIA/Q3/dados_climaticos.txt', encoding='ISO-8859-1')  


plt.plot(range(1, 13), macae_df['Tmin'], marker='o', label='Macaé - Tmin')
plt.plot(range(1, 13), macae_df['Tmax'], marker='o', label='Macaé - Tmax')
plt.plot(range(1, 13), macae_df['Tmedia'], marker='o', label='Macaé - Tmedia')
plt.xlabel('Mês')
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas em Macaé ao longo do ano')
plt.legend()
plt.grid(True)

# Salvar o gráfico de Macaé como uma figura
plt.savefig('macae_temperaturas.png')
plt.close()

# Repetir o processo para Rio de Janeiro
plt.figure(figsize=(10, 6))

# Lê os dados de Macaé e Rio de Janeiro em DataFrames


plt.plot(range(1, 13), rio_df['Tmin'], marker='o', label='Rio de Janeiro - Tmin')
plt.plot(range(1, 13), rio_df['Tmax'], marker='o', label='Rio de Janeiro - Tmax')
plt.plot(range(1, 13), rio_df['Tmedia'], marker='o', label='Rio de Janeiro - Tmedia')
plt.xlabel('Mês')
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas no Rio de Janeiro ao longo do ano')
plt.legend()
plt.grid(True)

# Salvar o gráfico do Rio de Janeiro como uma figura
plt.savefig('rio_temperaturas.png')
plt.close()
