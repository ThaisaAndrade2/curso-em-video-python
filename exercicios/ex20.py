import random
quant= 0
list = []

while quant < 4 :
    alunos = str(input("Digite o nome do aluno: "))
    list.append(alunos)
    quant += 1

ordenada = []
for x in range(0, 20):
    num = (random.randint(0, 3))
    if list[num] in ordenada:
        continue
    ordenada.append(list[num])

print( "Primeiro aluno: ", ordenada[0], "Segundo aluno: ",ordenada[1], "terceiro aluno: ",ordenada[2], "ultimo aluno: ",ordenada[3])

#print("O aluno que irá apagar o quadro é: ", list[num])