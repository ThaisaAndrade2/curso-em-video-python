#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua area e a quantidade de tinta necessaria
#para pinta-la sabendo que cada litro de tinta pinta uma area de 2m² - 4

altura = float(input("Digite a altura: "))
largura = float(input("Digite o comprimento: "))

area = (altura * largura)
tinta = area/2

print("sua parede tem {}X{}, para pinta-la é preciso {} litros de tinta!".format(altura, largura, tinta))
