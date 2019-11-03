import math
from match import

#Ctrl+Space - apresenta todos os itens da biblioteca
#import doce - importar toda biblioteca
#from doce import pudim - importa somente informações expecificas

print("{:-^20}".format("Aula - 08 - Módulos"))

num = int(input("Digite um número: "))
raiz = (math.sqrt(num))
print("A raiz quadrada de {} é {}".format(num, math.ceil(raiz)))
