x = int(input("Digite um número inteiro:"))

if (x % 3 == 0) and (x % 5 == 0):
    print("Seu número é divisível por 3 e por 5")
elif(x % 5 == 0):
    print("Seu número é divisível por 5")
elif (x % 3 == 0):
    print("Seu número é divisível por 3")
else:
    print(x)