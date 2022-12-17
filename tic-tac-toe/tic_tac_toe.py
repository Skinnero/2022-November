from board import Board
from game import Game
from menu import Menu
import os

if __name__ == "__main__":
    while True:
        table = Board()
        menu = Menu()
        menu.show_menu()
        player = menu.starting_player(menu.decision)
        table.display_board(table.board)

        # Human vs Human 
        while menu.decision == 1:

            hooman = Game()       
            table.mark_the_coord(table.board,hooman.hooman(),player)
            table.display_board(table.board)

            if  not table.is_full(table.board):
                break
            if table.check_terminal_case(table.board)[-1] == True:
                print(f'Player {table.check_terminal_case(table.board)[0]} won!')
                break

            player = menu.swap_player(player)
            
        # Random_AI vs Random_AI
        while menu.decision == 2:
            
            if player == None:
                player = 'O'
            ai = Game()
            table.mark_the_coord(table.board,ai.random_ai(),player)
            table.display_board(table.board)
            if table.check_terminal_case(table.board)[-1] == True:
                print(f'Player {table.check_terminal_case(table.board)[0]} won!')
                break
            if not table.is_full(table.board):
                print("It is Draw!")
                break
            player = menu.swap_player(player)
            input('Press any key to continue...')
            
            
            if not table.is_full(table.board):
                break
                
        # Human vs Random_AI
        hooman = player
        while menu.decision == 3:
            
            hooman_ai = Game()
            
            if hooman == 'O':
                table.mark_the_coord(table.board,hooman_ai.hooman(),player)
                table.display_board(table.board)    
            hooman = 'O'    
            
            if  not table.is_full(table.board):
                break
            if table.check_terminal_case(table.board)[-1] == True:
                print(f'Player {table.check_terminal_case(table.board)[0]} won!')
                break
            
            player = menu.swap_player(player)
            
            table.mark_the_coord(table.board,hooman_ai.random_ai(),player)
            table.display_board(table.board)

            
            if table.check_terminal_case(table.board)[-1] == True:
                print(f'Player {table.check_terminal_case(table.board)[0]} won!')
                break   
            if  not table.is_full(table.board):
                break
            
            player = menu.swap_player(player)

        # Human vs Unbeatable_AI
        while menu.decision == 4:
            
            hooman_uai = Game()
            if hooman == 'O':       
                table.mark_the_coord(table.board,hooman_uai.hooman(),player)
                table.display_board(table.board)
                player = menu.swap_player(player)
            hooman = 'O' 
                
            if  not table.is_full(table.board):
                break
            if table.check_terminal_case(table.board)[-1] == True:
                print(f'Player {table.check_terminal_case(table.board)[0]} won!')
                break
            
            if player == 'X':
                
                table.mark_the_coord(table.board,hooman_uai.unbeatable_ai_o_maximize(table.board,True,player)[1],player)
                table.display_board(table.board)
            else:
                table.mark_the_coord(table.board,hooman_uai.unbeatable_ai_x_maximize(table.board,player)[1],player)
                table.display_board(table.board)
            
            
            if table.check_terminal_case(table.board)[-1] == True:
                print(f'Player {table.check_terminal_case(table.board)[0]} won!')
                break   
            if  not table.is_full(table.board):
                break
            
            player = menu.swap_player(player)

        another_game = input("Do you want to play again? (y/n)")

        if another_game.lower() == 'y':
            os.system('clean')
            table.get_empty_board()
            continue
        
        else:
            print('Goodbye! o/\n')
            break

