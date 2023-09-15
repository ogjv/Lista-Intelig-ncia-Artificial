import numpy as np
import pandas as pd

def load_climatic_data_to_numpy():
    """
    Função para carregar dados climáticos para um NumPy array.
    """
    df = pd.read_excel("c:/Users/jvama/ListaIA/Q3/Dados_climaticos_historicos.xlsx", sheet_name="Historico_Clima_Rio_de_Janeiro", header=None)

    # Extraindo nomes dos meses da quarta linha (linha de índice 3)
    months = df.iloc[3, 1:13].tolist()
    
    # Extraindo dados de temperaturas das linhas 5, 6 e 7 e convertendo para float
    min_temperatures = [float(str(value).replace(',', '.')) for value in df.iloc[6, 1:13]]
    max_temperatures = [float(str(value).replace(',', '.')) for value in df.iloc[7, 1:13]]
    avg_temperatures = [float(str(value).replace(',', '.')) for value in df.iloc[5, 1:13]]
    
    # Criando um NumPy array de dimensão 12x3
    temperature_data = np.array([min_temperatures, max_temperatures, avg_temperatures]).T
    
    return months, temperature_data

def create_ascii_file(months, temperature_data):
    """
    Cria um arquivo ASCII com os dados de temperaturas.
    """
    with open("temperaturas_rio.txt", "w") as file:
        file.write("Mês\tTemperatura Mínima\tTemperatura Máxima\tTemperatura Média\n")
        for i in range(len(months)):
            file.write(f"{months[i]}\t{temperature_data[i, 0]}\t{temperature_data[i, 1]}\t{temperature_data[i, 2]}\n")

def main():
    months, temperature_data = load_climatic_data_to_numpy()
    
    create_ascii_file(months, temperature_data)
    
    print("Meses:", months)
    print("Temperaturas:")
    print(temperature_data)

    print("Dimensão (shape) do array de temperaturas:", temperature_data.shape)
    print("Máximo valor na coluna de temperatura média:", np.max(temperature_data[:, 2]))
    print("Mínimo valor na coluna de temperatura média:", np.min(temperature_data[:, 2]))

    # Restante das operações com NumPy
    sorted_indices = np.argsort(temperature_data[:, 2])
    reshaped_data = temperature_data.reshape(3, 12)
    transposed_data = temperature_data.transpose()
    concatenated_data = np.concatenate((temperature_data, temperature_data), axis=0)
    splitted_data = np.split(temperature_data, 3, axis=1)
    flipped_data = np.flip(temperature_data, axis=0)
    appended_data = np.append(temperature_data, [[1, 2, 3]], axis=0)
    deleted_data = np.delete(temperature_data, 0, axis=1)

if __name__ == "__main__":
    main()
