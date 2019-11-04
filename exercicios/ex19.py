import random
quant= 0
list = []

while quant < 4 :
    alunos = str(input("Digite o nome do aluno: "))
    list.append(alunos)
    quant += 1

num = (random.randrange(0, 3))
print("O aluno que irá apagar o quadro é: ", list[num])