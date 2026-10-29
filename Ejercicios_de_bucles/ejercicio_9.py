correcto = "contraseña"
x = 0
while x == 0:
    contra = input("introduce la contraseña: ")
    if contra.lower() == correcto:
        print("Acertaste la contraseña. Felicidades")
        x = x + 1
    else:
        print("Contraseña incorrecta. Sigue probando")