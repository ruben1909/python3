asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas = []
for asignatura in asignaturas:
    nota = int(input(f"que nota has sacado en {asignatura}: "))
    notas.append(nota)

for i in range(len(asignaturas) - 1,-1,-1):
    if notas[i] >= 5:
        del asignaturas[i]
        del notas[i]

print()
print("Asignaturas pendientes de aprobar")
for i in range(len(asignaturas)):
    print(f"Repites {asignaturas[i]} con un {notas[i]}")

# for asignatura in asignaturas[:]:
#     nota = float(input(f"¿Qué nota has sacado en {asignatura}?: "))
#     if nota >= 5:
#         asignaturas.remove(asignatura)

# print("Tienes que repetir:", asignaturas)
        