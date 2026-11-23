numeros = []
for i in range(6):
    num = int(input("escribe los numeros de la loteria: "))
    numeros.append(num)

array_ordenado = sorted(numeros)
# numeros.sort()
print (f"numeros ordenados de menor a mayor {array_ordenado}")