#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

n1 = int(input("Digite um número: "))
print("O dobro de {} é {}".format(n1, n1*2))
print("O triplo de {} é {}".format(n1, n1*3))
print("A raiz quadrada de {} é {}".format(n1, n1**(1/2)))
print("A raiz cubica de {} é {:.3f}".format(n1, n1**(1/3)))