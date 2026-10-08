prod = input ("introduce el nombre del producto: ")
precio = float(input("introduce el precio del producto: "))
unidades = int(input("introduce el numero de unidades: "))
precio_final = precio * unidades

print("{}: {:9.2f}€ x {:3d} unidades = {:11.2f}€".format(prod, precio, unidades, precio_final))

