cap = float(input("cantidad de dinero depositado: "))
cap_primer_año = round(cap *(1 + 0.04)**1,2)
cap_segundo_año = round(cap *(1 + 0.04)**2,2)
cap_tercer_año = round(cap *(1 + 0.04)**3,2)

print (f"la cantidad ahorrada el primer año sera de {cap_primer_año}€, de {cap_segundo_año}€ el segundo año y de {cap_tercer_año}€ el tercer año")