asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input(f"Que nota has sacado en {asignatura}: ")
    notas.append(nota)

print()
print("--------NOTAS-------")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

