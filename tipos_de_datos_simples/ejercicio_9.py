cap = float(input("cantidad a invertir(€): "))
interes = float(input("introduce el interes anual(%): "))
años = float(input("introduce  el numero de años: "))
cap_obtenido = cap*(interes/100)*años
cap_final = cap + cap_obtenido

print (f"el capital obtenido de la inversion es de {cap_obtenido}€ y el capital total es de {cap_final}€")