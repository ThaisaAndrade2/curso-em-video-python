#Faça um alooritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
prod = float(input("Qual preço do produto: "))
valor_desc =  prod * 0.05
desc = prod - valor_desc

print("O valor do produto R${}, com desconto de 5% é, R${}".format(prod, desc))