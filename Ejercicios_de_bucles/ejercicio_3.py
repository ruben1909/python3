numero = int(input("introduce un numero entero positivo: "))
num_imp = ""
for i in range(1,numero):
    if (i % 2) != 0:
        num_imp = num_imp + str(i) + ","
        
print(num_imp)