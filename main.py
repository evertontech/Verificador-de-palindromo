
print("Olá, gostaria de saber se uma palavra digitada é um palíndromo?")

palavraLimpa = str(input("Digite uma palavra: ")).lower().replace(' ', '')

palavraInvertida = palavraLimpa[::-1]

if palavraLimpa == palavraInvertida:
    print("Acertou!!!!! É um palíndromo")
else:
    print("INFELIZMENTE Não é um palíndromo. Tente novamente ", palavraLimpa)
