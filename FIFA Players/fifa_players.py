import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('E:\Python\FIFA Players/all_players_fifa.csv')

#criar o filtro
dadosselecionados = ['team','height','weight','age','name']

#usar a função do filtro para criar o novo objeto dataframe
dadosimportantes = dados.filter(items=dadosselecionados)

#criando um histograma para exibir alguma columa, "bins" são intervalor das colunas
dadosimportantes.hist(column='height', bins=30)
plt.show()