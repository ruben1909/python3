palabra = input("escribe una palabra: ")
if palabra == palabra[::-1]:
    print(f"La palabra {palabra} es palindromo")
else :
    print(f"La palabra {palabra} no es palindromo")