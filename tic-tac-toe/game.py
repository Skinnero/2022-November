from board import Board
from menu import Menu
import random

class Game(Board,Menu):
    
    def __init__(self):
        
        Board.__init__(self)
        Menu.__init__(self)
        
        
        # Logic in human vs human option
    def hooman(self):
        coords = []
        
        while True: 
            coords.append(input('Please provide a coordinates: '))
            if 'quit' in coords[-1].lower():
                quit()
            
            if coords[0].upper() not in ['A','B','C']:
                print('Out of bounds!')
                coords = []
                continue
            
            if len(coords) > 1:
                try:
                    if int(coords[1]) not in range(1,4):
                        print('Out of bounds!')
                        coords = []
                        continue
                except ValueError:
                    print('Out of bounds!')
                    coords = []
                    continue
            if len(coords) == 2:
                
                coords = self.translate_coords(coords)         
                if self.is_occupied(self.board,coords):
                    print('This place is occupied, try other one')
                    coords = []
                    continue
                
                return coords
        
        # logic for random AI         
    def random_ai(self):
        
        coords = self.get_empty_coords(self.board)
        ai_choice = random.choice(coords)
        return ai_choice
        
        # Room for improvement... i had to copy/paste same function cuz i couldn't make static value...
    def unbeatable_ai_o_maximize(self,board,minimaxing=False,player = 'O'): 
        
        if self.check_terminal_case(board)[0] == 'X' and self.check_terminal_case(board)[1] == True:
            return 1, None
        if self.check_terminal_case(board)[0] == 'O' and self.check_terminal_case(board)[1] == True:
            return -1, None
        if not self.is_full(board):
            return 0, None
        
        if minimaxing:
        
            max_grade = -100
            empty_space = self.get_empty_coords(board)
            best_move = None
            
            for row,col in empty_space:
                
                temp_board = board
                temp_board = self.mark_the_coord(temp_board,(row,col),player)
                grade = self.unbeatable_ai_o_maximize(temp_board,False,'O')[0]
                temp_board[row][col] = ' '
                if grade > max_grade:
                    max_grade = grade
                    best_move = (row, col)
                    
            return max_grade, best_move
            
        else:
            
            min_grade = 100
            empty_space = self.get_empty_coords(board)
            best_move = None
            
            for row,col in empty_space:
                temp_board = board
                temp_board = self.mark_the_coord(temp_board,(row,col),player)
                grade = self.unbeatable_ai_o_maximize(temp_board,True,'X')[0]
                temp_board[row][col] = ' '
                if grade < min_grade:
                    min_grade = grade
                    best_move = (row,col)
                    
            return min_grade, best_move

        # Room for improvement... i had to copy/paste same function cuz i couldn't make static value...
    def unbeatable_ai_x_maximize(self,board,minimaxing=False,player = 'X'):
        
        if self.check_terminal_case(board)[0] == 'O' and self.check_terminal_case(board)[1] == True:
            return 1, None
        if self.check_terminal_case(board)[0] == 'X' and self.check_terminal_case(board)[1] == True:
            return -1, None
        if not self.is_full(board):
            return 0, None
        
        if minimaxing:
        
            max_grade = -100
            empty_space = self.get_empty_coords(board)
            best_move = None
            
            for row,col in empty_space:
                
                temp_board = board
                temp_board = self.mark_the_coord(temp_board,(row,col),player)
                grade = self.unbeatable_ai_x_maximize(temp_board,False,'X')[0]
                temp_board[row][col] = ' '
                if grade > max_grade:
                    max_grade = grade
                    best_move = (row, col)
                    
            return max_grade, best_move
            
        else:
            
            min_grade = 100
            empty_space = self.get_empty_coords(board)
            best_move = None
            
            for row,col in empty_space:
                temp_board = board
                temp_board = self.mark_the_coord(temp_board,(row,col),player)
                grade = self.unbeatable_ai_x_maximize(temp_board,True,'O')[0]
                temp_board[row][col] = ' '
                if grade < min_grade:
                    min_grade = grade
                    best_move = (row,col)
                    
            return min_grade, best_move    
     