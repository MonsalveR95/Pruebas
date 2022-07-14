#Para crear un nuevo archivo .txt
# archivo = open("texto.txt", "a")
# archivo.write("Esto es una prueba de guardado")
# archivo.close()

#Para abrir el archivo en modo lectura
# archivo = open("texto.txt", "r")
# print(archivo.read())

#Crear funcion para encriptar y desencriptar texto

def encriptar(texto):
    #print("el texto a encriptar es: " + texto)
    textoFinal = ""
    for letra in texto:
        ascii = ord(letra)
        ascii += 1 
        textoFinal += chr(ascii)
    return textoFinal



def desencriptar(texto):
    #print("el texto a desencriptar es: " + texto)
    textoFinal = ""
    
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1 
        textoFinal += chr(ascii)
    return textoFinal


#desencriptar("Hxoxlxax xBxexbxéx")

def encriptarArchivo(rutaArchivo):
     archivo = open(rutaArchivo, "r")
     texto = archivo.read()
     archivo.close
     textoEncriptado = encriptar(texto)
     
     archivo = open(rutaArchivo, "w")
     archivo.write(textoEncriptado)
     archivo.close()
     print("El archivo se encriptó correctamente")


def desencriptarArchivo(rutaArchivo):
     archivo = open(rutaArchivo, "r")
     texto = archivo.read()
     archivo.close
     textoDesencriptado = desencriptar(texto)
     
     archivo = open(rutaArchivo, "w")
     archivo.write(textoDesencriptado)
     archivo.close()
     print("El archivo se desencriptó correctamente")


respuestaEoD = input("Presione 'E' para encriptar o 'D' para desencriptar: ")
rutaArchivo = input("Ingrese la ruta del archivo: ")

if respuestaEoD == "E":
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)
