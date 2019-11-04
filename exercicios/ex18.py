import math
ang = float(input("Digite o angulo: "))
seno = math.sin(math.radians(ang))
print("O seno do angulo {}° é {:.2f}".format(ang, seno))
cos = math.cos(math.radians(ang))
print("O cosseno do angulo {}° é {:.2f}".format(ang, cos))
tang = math.tan(math.radians(ang))
print("A tangente do angulo {}° é {:.2f}".format(ang, tang))