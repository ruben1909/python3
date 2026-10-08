fecha = input("introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
fecha_split = fecha.split("/")
print(f"naciste el dia {fecha_split[0]} del mes {fecha_split[1]} del año {fecha_split[2]}")
