#Faça um algoritmo que leia o salário de um funcionario e mostre sey novo salário com 15% de aumento
salario = float(input("Digite seu salário: "))
ajuste = (salario * 0.15) + salario
print("Você irá receber agora {:.2f} de ajuste salarial".format(ajuste))
