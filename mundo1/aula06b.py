print("---------Tipos primitivos---------")

n = input("digite algo:")
print("É númerico: ", n.isnumeric()) # É númerico ?
print("É caractere: ",n.isalpha()) # É caracteres ?
print("É um número/caratere", n.isalnum()) # É numero/caractere ?
print("É um conjunto de letras maiuscula: ",n.isupper()) # É letras maiuscula ?

print("--------Operador ternario----------")

isdecimal = n.isdecimal() and "sim" or "não"
isspace = n.isspace() and "sim" or "não"
istitle = n.istitle() and "sim" or "não"



#Chamando a variavél


print("O valor pode ser decimal ? {}".format(isdecimal))
print("O valor pode ser espaço ? {}".format(isspace))
print("O valor pode ser titulo ? {}".format(istitle))