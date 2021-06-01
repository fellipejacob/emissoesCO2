import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('E:/Python/Emissoes CO2/CO2Emission_LifeExp.csv')

dadosselecionados = dados.filter(items=['Country', 'CO2Emissions','LifeExpectancy'])

expectativaVSco2 = dadosselecionados.groupby(['LifeExpectancy','Country'], as_index=False).mean()
print(expectativaVSco2.sort_values('LifeExpectancy', ascending= False))

expectativaVSco2.to_excel('expectativaVSco2.xlsx')


#ainda falta plotar de uma forma digna