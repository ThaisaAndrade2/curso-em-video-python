print("------Operadores aritiméticos -----")

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# // Divisão inteira
# ** Potenciação
# % Modulo - Resto da Divisão

print ("-------Exemplo-------")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
poten = n1 ** n2
mod =  n1 % n2

print("A soma é {}".format(soma))
print("A subtração é {}".format(sub))
print("A multiplicação é {}".format(mult))
print("A divisão é {}".format(div))
print("A divisão inteira é {}".format(div_int))
print("A potenciação é {}".format(poten))
print("O modulo é {}".format(mod), end=" ")

print("A soma é {}, o produto é {} e divisão é {:.3f}".format(soma, mult , div  ))


#ORDEM DE PRECEDÊNCIA
# ()
# **
# *  /  //  %
# +  -

