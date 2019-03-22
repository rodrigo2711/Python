import math

ca = float(input("Cateto Adjacente = "))
co = float(input("Cateto Oposto = "))
s1 = math.pow(ca,2) + math.pow(co,2)
print("A hipotenusa é {}" .format(math.sqrt(s1)))