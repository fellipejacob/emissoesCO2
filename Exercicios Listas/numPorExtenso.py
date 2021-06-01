#usuário deve digitar um número de 0 a 10 
#e o programa retornar o mesmo por extenso;

numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True: 
    n = int (input("Digite um número entre 0 e 10: "))
    if 0 <= n <= 10:
        break
    print('Tente novamente. ', end="")

print (f"Voce digitou o número {numero[n]}.")