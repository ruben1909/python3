#correo-ejemplo@gmail.com
correo_usu = input("introduce un correo electronico: ")
correo_split = correo_usu.split("@")
correo_final = correo_split[0] + "@ceu.es"
print (f"{correo_final}")
