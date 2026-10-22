pizza_pregunta = input("¿Quieres tu pizza vegetariana?(elige SI o NO): ")
vege = "1 Pimiento \n2 Tofu"
no_vege = "1 Peperoni \n2 Jamón \n3 Salmón"
pizza = "mozzarella,tomate,"

if pizza_pregunta.lower() == "si":
    print(f"{vege}")
    ingrediente =  int(input ("elige uno de los ingredientes: "))
    if ingrediente == 1 :
        pizza = pizza + "Pimiento"
    if ingrediente == 2 :
        pizza = pizza + "Tofu" 
    print (f"tu pizza es vegetariana y lleva los siguientes ingredientes: {pizza}")

if pizza_pregunta.lower() == "no":
    print(f"{no_vege}")
    ingrediente = int(input ("elige uno de los ingredientes: "))
    if ingrediente == 1 :
        pizza = pizza + "Peperoni"
    if ingrediente == 2 :
        pizza = pizza + "Jamon" 
    if ingrediente == 3 :
        pizza = pizza + "Salmon" 
    print (f"tu pizza no es vegetariana y lleva los siguientes ingredientes: {pizza}")




