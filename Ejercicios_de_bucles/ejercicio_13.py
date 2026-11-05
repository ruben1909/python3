a = 0
while a == 0 :
    usu = input("introduce una palabra: ")
    if usu.lower() == "salir":
        a = a + 1
    else:
        print(usu)