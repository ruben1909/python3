sexo = input("introduce tu sexo (M o F): ")
nombre = input("introduce tu nombre: ")

if nombre < "m" and sexo.lower() == "f":
    print("te corresponde el grupo A")
if nombre > "m" and sexo.lower() == "f":
    print("te corresponde el grupo B")

if nombre > "n" and sexo.lower() == "m":
    print("te corresponde el grupo A")
if nombre < "n" and sexo.lower() == "m":
    print("te corresponde el grupo B")
