import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('E:\Python\FIFA Players/all_players_fifa.csv')

#criar o filtro
dadosselecionados = ['team','height','weight','age','name']

#usar a função do filtro para criar o novo objeto dataframe
dadosimportantes = dados.filter(items=dadosselecionados)

#criando um histograma para exibir alguma columa, "bins" são intervalor das colunas
# dadosimportantes.hist(column='height', bins=30)
# plt.show()

#conceito do boxplot:
#LS(limite superior) = Q3 + 1,5.(Q3-Q1)
#LI(Limite inferior) = Q1 -1,5.(Q3-Q1)
#onde Q1 é a mediana dos dados inferiores e Q3 é a mediana dos dados superiores


#criando um boxplot para analise dos outliers
# dadosimportantes.boxplot(column=['age','height','weight'])
# plt.show()

#criando um novo dataframe usando um teste verifica True or False para o critério:
brasileiros = dadosimportantes.loc[dadosimportantes['team'] == 'Brazil']

altura = brasileiros['height']
peso = brasileiros['weight']

plt.scatter(altura,peso)
plt.show()