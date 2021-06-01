num = int (input ("Digite a quantidade de números para analisar: "))
result = [n for n in range(num) if n % 3 == 0 and n % 5 == 0]
print (result)