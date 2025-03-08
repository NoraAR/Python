def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------"*3,"+", sep="")
    for i in range(3):
        print(f"|       "*3 ,"|" ,sep="")
        for j in range(3):
            print(f"|   {board[i][j]}   ", end="")
        print("|")
        print(f"|       "*3 ,"|" ,sep="")
        print("+-------"*3,"+", sep="")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    state=True
    while(state):
        try:
            user_movement = int(input("Ingresa un movimiento: "))
        except valueError as e:
            print("¡El movimiento que ingresaste no es valido!")
            continue
        if user_movement in board:
            for i in range(3):
                for j in range(3):
                    board[i][j] = user_movement
                    state=False
        else:
            print("¡El movimiento que ingresaste no es valido!")
    display_board(board)
    
#def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    
    
#def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.


#def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.

board = []
val = 1

for i in range(3):
    rows = [0]*3
    for j in range(3):
        rows[j] = val
        val += 1
    board.append(rows)

enter_move(board)
