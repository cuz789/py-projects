"""TIC-TAC-TOE GAME"""


def tictactoe(row1,row2,row3):
    #OUTLINE
    print(row1)
    print(row2)
    print(row3)
    
def userinput():
    #USER INPUT X or O
    s = input('Enter your choice X or O :')
    acceptable_values = ['X', 'O']
    while s not in acceptable_values:
        s = input('Enter PROPER VALUE:')
    return s
    
def input_position(row1, row2, row3, value):
    #USER INPUT WITH POSITION SELECTION
    tictactoe(row1, row2, row3)
    rows = { '1' : row1, '2' : row2, '3' : row3}
    available_positions = ['0','1','2']
    available_rows = ['1','2','3']
    rn  = input('Enter row numbers (1, 2, or 3):')
    while rn not in available_rows:
        print('Invalid row number.')
        rn = input('Enter row number (1, 2, or 3): ')
        
    p = input('Enter your position (0, 1, or 2):')
    
    while p not in available_positions:
        print('Invalid position.')
        p = input('Enter your position (0, 1, or 2): ')
        
    if rows[rn][int(p)] == ' ':
        rows[rn][int(p)] = value
    else:
        print('Input cannot be modified')
    
def game(row1, row2, row3):
    #CHECK ROWS
    for row in [row1, row2, row3]:
        if row[0] == row[1] == row[2] != ' ':
            print(f' winner {row[0]}')
            return True

    #CHECK COLOUMNS
    for i in range(3):
        if row1[i] == row2[i] == row3[i] != ' ':
            print(f' winner {row1[i]}')
            return True

    # CHECK DIAGONALS
    if row1[0] == row2[1] == row3[2] != ' ':
        print(f' winner {row1[0]}')
        return True
    if row1[2] == row2[1] == row3[0] != ' ':
        print(f' winner {row1[2]}')
        return True
    return False

def playgame():
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    Player1 = userinput()
    
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'
    while game(row1,row2,row3) == False:
        input_position(row1, row2, row3, Player1)
        if game(row1, row2, row3):
            break
        input_position(row1, row2, row3, Player2)
    return tictactoe(row1,row2,row3)

#Run Game
playgame()
        
        
        
    
     
    

    
