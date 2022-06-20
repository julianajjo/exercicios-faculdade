num = int(input())

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(num):
    print(letras[i]*(i+1))


# OUTRA RESOLUÇÃO:
# num = int(input())
# letra = 'A'

# for linha in range(1, num+1):
#     print(letra * linha)
#     letra = chr(ord(letra) + 1)

# A função ord pegará a letra e irá transformá-la em código unicode e somará 1
# Em seguida irá converter o unicode em caracter novamente
# Com essa conversão não é necessário digitar o alfabeto inteiro
