import pandas as pd
import numpy as np

#transformando um dicionário em DATAFRAME com PANDAS
alunos = {'Nome': ['Alberto','Fellipe','André','Ricardo','Matheus'],
          'Nota': [6,7,8,9,10],
          'Aprovado':['Não','Não','Sim','Sim','Sim']}
dataframe = pd.DataFrame(alunos)
print (dataframe)

#criando uma SERIES no PANDAS
objeto1 = pd.Series ([1,2,3,4])
print (objeto1)

#transformando um ARRAY em SERIES no PANDAS
array = np.array([1,2,3,4,5])
print (array)

objeto2 = pd.Series(array)