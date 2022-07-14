pages = [
    "pag 0) Era una noche fría en la ciudad...\n elige como sigue la historia \n 1)... \n 2)... \n 3)...",
    "pag 1) Era una noche fría en la ciudad...\n elige como sigue la historia \n 1)... \n 2)... \n 3)...",
    "pag 2) Era una noche fría en la ciudad...\n elige como sigue la historia \n 1)... \n 2)... \n 3)...",
]

def showPag(pageNumber):
    text = pages[pageNumber]
    print(text)
    respue= input()
    showPag(int(respue))

showPag(0)