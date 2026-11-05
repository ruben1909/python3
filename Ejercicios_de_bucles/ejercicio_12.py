frase = input("introduce una frase: ")
letra = input("introduce una letra: ")
contador = 0
for i in frase:
    if letra == i:
        contador = contador + 1
print(f"en la frase '{frase}' esta la letra '{letra}' {contador} veces")