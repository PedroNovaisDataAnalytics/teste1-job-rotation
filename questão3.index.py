import pandas as pd
import json

# Lendo o arquivo JSON com os dados de faturamento diário
with open('basededados.json') as json_file:
    dados_faturamento = json.load(json_file)

# Convertendo os dados para um DataFrame do Pandas
df_faturamento = pd.DataFrame(dados_faturamento)

# Extraindo o menor e o maior valor de faturamento ocorrido em um dia do mês
menor_faturamento = df_faturamento['valor'].min()
maior_faturamento = df_faturamento['valor'].max()

# Calculando a média mensal de faturamento, ignorando os dias sem faturamento
media_mensal = df_faturamento[df_faturamento['valor'] > 0]['valor'].mean()

# Calculando o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len(df_faturamento[df_faturamento['valor'] > media_mensal])

# Imprimindo os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Média mensal de faturamento: R${media_mensal:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
