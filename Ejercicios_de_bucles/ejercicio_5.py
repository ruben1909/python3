cap = float(input("cantidad a invertir(€): "))
interes = float(input("introduce el interes anual(%): "))
años = int(input("introduce  el numero de años: "))
for i in range(1,años+1):
    cap_obtenido = cap*(interes/100)*i
    cap_final = cap + cap_obtenido
    print(f"el capital obtenido el año {i} es de {cap_obtenido} y capital total de la inversion es {cap_final}")
