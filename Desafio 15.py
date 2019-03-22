km = int(input("Quantidade de km percorrido? "))
dias = int(input("Quantidade de dias? "))
custo1 = 60*dias
custo2 = 0.15*km
print("O total a pagar é R$ {:.2f}" .format(custo1+custo2))
