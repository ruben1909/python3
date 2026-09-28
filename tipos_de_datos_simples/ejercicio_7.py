peso = float(input("introduce tu peso en kilogramos: "))
estatura = float(input("introduce tu estatura en metros: "))
imc = round(peso / (estatura**2),2)
print(f"tu imc es de {imc}")
