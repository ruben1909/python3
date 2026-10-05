#+34-913724710-56
telf_usu = input("introduce tu numero de telefono: ")
telf_split = telf_usu.split("-")
telf_final = telf_split[1]
print(f"el numero de telefono sin el prefijo ni la extension es {telf_final}")
