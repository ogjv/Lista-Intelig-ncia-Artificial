import pandas as pd

# Ler o arquivo Excel com as abas desejadas
xls = pd.ExcelFile("c:/Users/jvama/ListaIA/Q3/Dados_climaticos_historicos.xlsx")
macae_df = pd.read_excel(xls, sheet_name="Historico_Clima_Macae")
rio_df = pd.read_excel(xls, sheet_name="Historico_Clima_Rio_de_Janeiro")

# Transpor o DataFrame para que os meses se tornem índices das colunas
macae_df = macae_df.transpose()
rio_df = rio_df.transpose()

# Definir os nomes das colunas para Macaé e Rio de Janeiro
colunas = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Definir os meses como índice
macae_df.columns = colunas
rio_df.columns = colunas

# Remover as últimas linhas que contêm informações de referência
macae_df = macae_df.iloc[:-1]
rio_df = rio_df.iloc[:-1]

# Converter as colunas de temperatura para float
macae_df = macae_df.apply(pd.to_numeric, errors='coerce')
rio_df = rio_df.apply(pd.to_numeric, errors='coerce')

# Calcular a média anual para cada conjunto de registro de temperaturas
macae_media_anual = macae_df[colunas].mean().mean()
rio_media_anual = rio_df[colunas].mean().mean()

# Exibir a média anual
print("Média Anual em Macaé:", macae_media_anual)
print("Média Anual no Rio de Janeiro:", rio_media_anual)
