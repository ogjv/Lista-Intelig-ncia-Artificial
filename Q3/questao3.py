import pandas as pd

def read_climatic_data():
    """
    Função para ler dados climáticos de um arquivo Excel e retornar 4 listas: meses, temperaturas mínima, máxima e média.
    """
    # Lê os dados do arquivo Excel
    df = pd.read_excel("c:/Users/jvama/ListaIA/Q3/Dados_climaticos_historicos.xlsx", sheet_name="Historico_Clima_Macae", header=None)

    # Extrair nomes dos meses da quarta linha (linha de índice 3)
    months = df.iloc[3, 1:13].tolist()
    
    # Extrair dados de temperaturas das linhas 5, 6 e 7
    min_temperatures = df.iloc[4, 1:13].tolist()
    max_temperatures = df.iloc[5, 1:13].tolist()
    avg_temperatures = df.iloc[6, 1:13].tolist()
    
    return months, min_temperatures, max_temperatures, avg_temperatures

def create_climatic_dictionary(months, min_temperatures, max_temperatures, avg_temperatures):
    """
    Função para criar um dicionário de dados a partir das 4 listas fornecidas.
    """
    climatic_data = {}
    for i in range(len(months)):
        month_data = {
            "Tmin": min_temperatures[i],
            "Tmax": max_temperatures[i], 
            "Tmedia": avg_temperatures[i]
        }
        climatic_data[months[i]] = month_data
    return climatic_data

def write_to_ascii_file(months, min_temperatures, max_temperatures, avg_temperatures):
    """
    Função para escrever os dados em um arquivo ASCII.
    """
    with open("dados_climaticos.txt", "w") as file:
        file.write("Mês Tmin Tmax Tmedia\n")
        for i in range(len(months)):
            # Escreve os dados em formato de tabela
            file.write(f"{months[i]} {min_temperatures[i]} {max_temperatures[i]} {avg_temperatures[i]}\n")

def main():
    # Lê os dados climáticos do Excel
    months, min_temperatures, max_temperatures, avg_temperatures = read_climatic_data()
    
    # Cria um dicionário de dados climáticos
    climatic_dict = create_climatic_dictionary(months, min_temperatures, max_temperatures, avg_temperatures)

    # Escreve os dados em um arquivo ASCII
    write_to_ascii_file(months, min_temperatures, max_temperatures, avg_temperatures)
    
    # Exibe o conteúdo do dicionário de dados climáticos
    print("Dicionário de dados climáticos:")
    for month, data in climatic_dict.items():
        print(f"{month}: Tmin={data['Tmin']}, Tmax={data['Tmax']}, Tmedia={data['Tmedia']}")

    # Calcula e exibe a temperatura média do mês de julho
    july_avg_temperature = climatic_dict["Julho"]["Tmedia"]
    print(f"Temperatura média do mês de julho: {july_avg_temperature}")

if __name__ == "__main__":
    main()
