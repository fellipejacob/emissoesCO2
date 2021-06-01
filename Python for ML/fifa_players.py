import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/HENRRIQUE/OneDrive/Documentos/pandas_files/all_players_fifa.csv')

print(dados.sort_values('caps'))