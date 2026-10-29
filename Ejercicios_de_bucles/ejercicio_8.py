num = int(input("introduce un numero: "))
for x in range (1,num+1,2):
    for i in range (x,0,-2):
        print (i, end=" ")
    print()
    