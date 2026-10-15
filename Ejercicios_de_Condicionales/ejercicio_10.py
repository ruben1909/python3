pizza = input("¿Quieres tu pizza vegetariana?(elige SI o NO): ")
vege = "Pimiento,Tofu"
vege_split = vege.split(",")
no_vege = "Peperoni,Jamón,Salmón"

if pizza.lower() == "si":
    print(f"{vege}")
if pizza.lower() == "no":
    print(f"{no_vege}")

