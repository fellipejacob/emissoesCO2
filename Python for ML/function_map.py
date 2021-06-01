tempC = [0,5,12,17,23,25,28,30,35,42]

#função MAP serve para mapear os elementos de uma lista determinada sem usar o laço FOR.
#determinar primeiro a função a ser aplicada e depois de onde os dados devem ser extraídos.
#para incluir em uma lista, usar a função LIST antes do MAP
tempF = list(map(lambda x : (x*1.8) + 32, tempC))
print (tempF) 

#exemplo com números para obter o dobro:
nums = [1,2,3,4,5,6,7,8,9]
dobro = list(map(lambda x : x*2, nums))
print (dobro)