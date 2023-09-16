import matplotlib.pyplot as plt


# 1. Use o comando open para ler os dados do arquivo de texto
months = []
min_temperatures = []
max_temperatures = []
avg_temperatures = []

with open("c:/Users/jvama/ListaIA/Q3/dados_climaticos.txt", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:  # Ignorar a primeira linha (cabeçalho)
        data = line.strip().split()  # Dividir a linha em palavras
        months.append(data[0])
        min_temperatures.append(float(data[1]))
        max_temperatures.append(float(data[2]))
        avg_temperatures.append(float(data[3]))

# 2. Montar um dicionário de dados
climatic_data = {}
for i in range(len(months)):
    month_data = {
        "Tmin": min_temperatures[i],
        "Tmax": max_temperatures[i], 
        "Tmedia": avg_temperatures[i]
    }
    climatic_data[months[i]] = month_data

# 3. Exibir o conteúdo do dicionário
print("Dicionário de dados climáticos:")
for month, data in climatic_data.items():
    print(f"{month}: Tmin={data['Tmin']}, Tmax={data['Tmax']}, Tmedia={data['Tmedia']}")

# 4. Exibir a temperatura média de julho
july_avg_temperature = climatic_data["Julho"]["Tmedia"]
print(f"Temperatura média do mês de julho: {july_avg_temperature}")

# 5. Plotar um gráfico de temperatura
plt.figure(figsize=(10, 6))
plt.plot(months, min_temperatures, marker='o', label='Tmin')
plt.plot(months, max_temperatures, marker='o', label='Tmax')
plt.plot(months, avg_temperatures, marker='o', label='Tmedia')
plt.xlabel('Meses')
plt.ylabel('Temperatura')
plt.title('Temperaturas Mensais')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
