# edad1 = 71
# if not(edad1 < 18 or edad1 >= 70):
#     print("Puede entrar al sitio")
# else:
#     print("Prueba en otro sitio")

# nombre = input("¿cómo te llamas? ")

# print("Hola " + nombre) 

# edad = int(input("Ingresa tu edad "))

# masDe18 = edad>= 18 
# esHijoDelDueño= input("¿Eres hijo del dueño? ")
# respuesta = esHijoDelDueño == "si"
# puedepasar = masDe18 or respuesta

# if puedepasar:
#     print("Puede entrar al sitio")
# else:
#     print("Prueba en otro sitio")

# x = int(input("ingresa un número "))

# if x % 2 == 0:
#     print("Es un par")
# else:
#     print("No es par")   

def Mpreciofinal(producto, precio, descuento):
    preciofinal = precio - precio*descuento/100
    print("El precio del " + producto + " es $ " + str(preciofinal))

Mpreciofinal("Libro", 50000, 25)


