puntos = float(input("introduce la puntuacion del empleado: "))

if puntos != 0.0 and puntos != 0.4 and puntos < 0.6:
    print("puntos invalidos")
if puntos == 0.0:
    print("no tienes bonificacion")
if puntos == 0.4:
    bono = puntos * 2400
    print(f"tienes una bonificacion de {bono}€")
if puntos >= 0.6:
    bono = puntos * 2400
    print(f"tienes una bonificacion de {bono}€")