nums = [int(input("Digite o número:")) for i in range(5)]

#dentro de uma estrutura de lista, se cria uma variável varrendo a lista, após definir a função.
#ESTRUTURA -> (FUNÇÃO) FOR - VARIAVEL - IN - LISTA
dobro = [(x*2) for x in nums]
print(dobro)


#usuário digita a frase e retorna uma lista com os caracteres da frase;
frase = [i for i in (str(input("Digite uma frase: ")))]
print (frase)