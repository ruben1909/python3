primo = 0
num = int(input("introduce un numero: "))
for x in range (1,num + 1):
    if num % x == 0 :
        primo = primo + 1

if primo <= 2:
    print(f"el numero {num} es primo")
else :
    print(f"el numero {num} NO es primo")