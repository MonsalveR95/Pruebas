seguirchateando = True
while seguirchateando:

    texto = input(">")
    if texto == "salir":
       seguirchateando = False 
    texto =texto.replace(":)", "🙂")
    texto =texto.replace(":*", "😘")
    texto =texto.replace(":p", "😛")
    texto =texto.replace(":P", "😛")
    texto =texto.replace(":(", "😞")
    print(texto) 

#\N{slightly smiling face}

