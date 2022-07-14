"""
wordle.py
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _
_ _ _ _ _ _

palabra == intento -> Ganar!
letra in palabra  -> Ayuda!
letra not in palabra -> No existe

Otras reglas que no se van a hacer
la palabra existe dentro de la lista de posibles palabras. 
"""
colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'ENDC': '\033[0m',
}

def color_letter(letter, color):
    return colors[color] + letter + colors["ENDC"]


# init game
print("Wordle.py emepezar!")

win = False
word = "trineo"
board = []
for i in range(6):
    board.append(["_" for l in range(6)])

game_loop_counter = 0 
while (not win) and (game_loop_counter < len(word)): 
    text = input("")
    while len(text) != len(word):
        print(f"La palabra debe tener {len(word)} de longitud")
        text = input("")

    #win logic
    if word == text:
        board[game_loop_counter] = [l for l in text]
        win = True

    #letter in word 
    else: 
        test_line = []
        for j in range(len(text)):
            if text[j] == word[j]:
                test_line.append(text[j])
            elif text[j] in word:
                test_line.append(color_letter( text[j], 'yellow'))
            else:
                test_line.append(color_letter( text[j], 'red'))

        board[game_loop_counter] = test_line




    #Draw (Dibuja el tablero)
    for i in range(6):
        print(" ".join(board[i])) 

    game_loop_counter += 1 
if win: 
    print("Siuuuu")
else: 
    print("Noooo")
    #some