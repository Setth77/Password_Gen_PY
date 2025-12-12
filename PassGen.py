import random

caracteres = ('a','a','b','b','c','c','d','d','e','e','f','f','g','g','h','h',
              'i','i','j','j','k','k','l','l','m','m','n','n','o','o','p','p',
              'q','q','r','r','s','s','t','t','u','u','v','v','w','w','x','x',
              'y','y','z','z','A','A','B','B','C','C','D','D','E','E','F','F',
              'G','G','H','H','I','I','J','J','K','K','L','L','M','M','N','N','O','O',
              'P','P','Q','Q','R','R','S','S','T','T','U','U','V','V','W','W','X','X',
              'Y','Y','Z','Z','0','0','1','1','2','2','3','3','4','4','5','5','6','6','7','7',
              '8','8','9','9')

entrada = input("qual o tamanho da senha 1-9: ")
tamanho = int(entrada)
senha = ""

for i in range(tamanho):
    indice = random.randint(0, len(caracteres) - 1)
    senha += caracteres[indice]


print("\nSua senha gerada é:")
print(senha)

