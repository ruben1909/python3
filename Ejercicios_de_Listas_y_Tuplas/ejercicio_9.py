palabra = input("introduce una palabra: ")
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in palabra:
    match letra:
        case "a":
            contador_a = contador_a + 1
        case "e":
            contador_e = contador_e + 1
        case "i":
            contador_i = contador_i + 1
        case "o":
            contador_o = contador_o + 1
        case "u":
            contador_u = contador_u + 1

print (f"a : {contador_a} veces")
print (f"e : {contador_e} veces")
print (f"i : {contador_i} veces")
print (f"o : {contador_o} veces")
print (f"u : {contador_u} veces")



