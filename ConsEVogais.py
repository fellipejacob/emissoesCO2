word = str (input("Digite uma palavra: "))

def contaVogais(word):
    word = word.lower()
    vogais = 'aeiou'
    return {i: word.count(i) for i in vogais if i in word}
def contaConsoante(word):
    word = word.lower()
    consoantes = 'qwrtypsdfghjklzxcvbnmç'
    return {i: word.count(i) for i in consoantes if i in word}
    
    
print ("Vogais:",contaVogais(word),"\nConsoantes:",contaConsoante(word))