import math
ctt_opost = float(input("Digite o valor do cateto oposto: "))
ctt_adjacen = float(input("Digite o valor do cateto ajdacente: "))
hpt = math.pow(ctt_opost, 2) + math.pow(ctt_adjacen, 2)
result = math.sqrt(hpt)
print(" A hipotenusa é {:.2f} ".format(result))