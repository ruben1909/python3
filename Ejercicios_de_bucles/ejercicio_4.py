numero = int(input("introduce un numero entero positivo: "))
cuenta_atras = ""
for i in range(numero,0-1,-1):
    cuenta_atras = cuenta_atras + str(i) + ","
        
print(cuenta_atras)