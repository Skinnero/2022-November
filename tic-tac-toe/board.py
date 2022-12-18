class Board:
       
    def __init__(self, board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]):
        self.board = board
        
        
        # Resets board to empty spaces, returns board
    def get_empty_board(self):
        for col in range(3):
            for row in range(3):
                self.board[col][row] = ' '
        return self.board        
    

        # Check if board is full and returns True if it's not
    def is_full(self,board):
        for col in range(3):
            for row in range(3):
                if board[col][row] == ' ':
                    return True
        return False
    
        # Marks the specified spot chosen by a player, returns marked board
    def mark_the_coord(self,board,coordinates,player):
        row,col = coordinates
        board[row][col] = player
        return board
    
        # Terminal case, returns value and True if terminal case otherwise None,False
    def check_terminal_case(self,board):
        
        # Vertical Check
        for row in range(3):
            counter = []
            for col in range(3):
                if board[row][0] == board[row][col]:
                    counter.append(board[row][col])
                if len(counter) == 3 and ' ' not in counter:
                    return counter[0], True
            
        # Horizontal Check
        for row in range(3):
            counter = []
            for col in range(3):
                if board[0][row] == board[col][row]:
                    counter.append(board[col][row])
                if len(counter) == 3 and ' ' not in counter:
                    return counter[0], True
            
        # Diagonal Check
        counter_forward = []
        counter_backward = []
        
        for row in range(3):
            if board[2][0] == board[2-row][row]:
                counter_forward.append(board[2-row][row])
            if board[0][0] == board[row][row]:
                counter_backward.append(board[row][row])
            if len(counter_backward) == 3 and ' ' not in counter_backward:
                return counter_backward[0], True
            if len(counter_forward) == 3 and ' ' not in counter_forward:
                return counter_forward[0], True
        
        return None, False

        # Displays board
    def display_board(self,board):
        
        print('\n         1   2   3 ')
        print(f'\n     A   {board[0][0]} | {board[0][1]} | {board[0][2]}')
        print('        ---+---+---')
        print(f'     B   {board[1][0]} | {board[1][1]} | {board[1][2]}')
        print('        ---+---+---')
        print(f'     C   {board[2][0]} | {board[2][1]} | {board[2][2]}\n')
        
        # Checks if spot is occupied, return True if not occupied
    def is_occupied(self, board, coordinates):
        x,y = coordinates
        if board[x][y] == ' ':
            return False
        else:
            return True
        
        # Returns only empty coordinates to the list
    def get_empty_coords(self,board):
        empty_coord = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ' ':
                    empty_coord.append([row,col])
        
        return empty_coord
    
        # Return integer value of coordinates in list
    def translate_coords(self,coords):
        
        if coords[0].upper() == 'A':
            coords[0] = 0
        elif coords[0].upper() == 'B':
            coords[0] = 1
        elif coords[0].upper() == 'C':
            coords[0] = 2
        
        coords[1] = int(coords[1]) -1    
        
        return coords
        