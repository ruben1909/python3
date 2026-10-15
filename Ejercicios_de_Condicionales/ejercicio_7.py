renta = float(input("introduce tu renta anual: "))

if renta < 10000 :
    print("impositivo del 5%")
if renta >= 10000 and renta < 20000 :
    print("impositivo del 15%")
if renta >= 20000 and renta < 35000 :
    print("impositivo del 20%")
if renta >= 35000 and renta < 60000 :
    print("impositivo del 30%")
if renta >= 60000 :
    print("impositivo del 45%")