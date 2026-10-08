precio = input("introduce un precio de un producto: ")
precio_split = precio.split(".")
print (f"el numero de euros es de {precio_split[0]}€ y el numero de centimos es de {precio_split[1]} centimos")
