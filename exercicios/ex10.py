#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quandos dolares ela pode comprar
#pega o valor da pessoa e dividir por 3.27

din = float(input("Digite quantos reais tem na sua carteira: "))
print("Você pode comprar com {}, {:.2f} dolares".format(din, din / 3.27))