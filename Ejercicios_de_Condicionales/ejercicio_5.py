edad = int(input("introduce tu edad: "))
ingresos = float(input("introduce tus ingresos mesuales(€): "))

if edad >= 16 and ingresos >=1000:
    print("si tributa")
else:
    print("no tributa")