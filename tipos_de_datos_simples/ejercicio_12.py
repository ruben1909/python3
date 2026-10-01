precio_pan = 3.49
precio_no_dia = round(precio_pan - (precio_pan*0.6),2)
num_ventas = int(input("introduce el numero de barras de pan vendidas que no son del dia: "))
coste_final = round(precio_no_dia * num_ventas,2)
print (f"el precio habitual de una barra de pan es de {precio_pan}€ y el precio por no ser fresca es de {precio_no_dia}€ y el coste total de las barras de pan vendidas que no son frescas es de {coste_final}€")

