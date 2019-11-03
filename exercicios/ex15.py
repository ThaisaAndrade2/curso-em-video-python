km = float(input("Quantos km você percorreu com o carro: "))
dias = int(input("Quantos dias alugou: "))
somad = 60 * dias
somak = 0.15 * km
total = somad + somak

print("O valor que você deve pagar é {}: ".format(total))