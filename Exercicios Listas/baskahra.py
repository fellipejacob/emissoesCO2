import math

a = int (input("Digite a variável a: "))
b = int (input("Digite a variável b: "))
c = int (input("Digite a variável c: "))

delta = b**2 - (4*a*c)

#se delta é menor que 0, não existe raiz real
if delta < 0:
    print("Não existem raízes reais.")


#se delta é igual a 0, só existe uma raíz real 
elif delta == 0:
    x1 = (-b )/(2*a)
    print ("A equação possui apenas uma raiz real, que é ","%.2f" %x1)
#lembrar sempre de usar o %.2f pra referenciar variável


elif delta > 0:
    rDelta = math.sqrt (delta)
    x1 = (-b - rDelta)/(2*a)
    x2 = (-b + rDelta)/(2*a)
    print("As raízes são ", "%.2f" %x1," e ","%.2f" %x2)