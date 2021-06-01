import pandas as pd

alunosDIC = {'Nome': ['Alberto','Fellipe','André','Ricardo','Matheus'],
          'Nota': [6,7,8,9,10],
          'Aprovado':['Não','Não','Sim','Sim','Sim']}

alunosDF = pd.DataFrame(alunosDIC)
#conta o número de linhas e colunas
print (alunosDF.shape)

#filtra por colunas específicas, usando o nome da coluna
print (alunosDF['Nome'])

#filtra por linhas, usando o número da linha
print (alunosDF.loc[1:3])

