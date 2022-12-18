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
        hooman = player
        if player == 'X':
            player = menu.swap_player(player)
        print(f"{'': >4}Player '{player}' will be moving!")
        table.display_board(table.board)
        # Human vs Human 
        while menu.decision == 1:

            hooman = Game()       
            table.mark_the_coord(table.board,hooman.hooman(),player)
            player = menu.swap_player(player)
            print(f"{'': >4}Player '{player}' will be moving!")
            table.display_board(table.board)

            if table.check_terminal_case(table.board)[-1] == True:
                print(f"{'': >6}Player {table.check_terminal_case(table.board)[0]} won!\n")
                break
            if  not table.is_full(table.board):
                print(f"{'': >6}It's a Draw!")
                break
        
            
        # Random_AI vs Random_AI
        while menu.decision == 2:
            
            ai = Game()

            table.mark_the_coord(table.board,ai.random_ai(),player)
            player = menu.swap_player(player)
            print(f"{'': >4}Player '{player}' will be moving!")
            table.display_board(table.board)
            if table.check_terminal_case(table.board)[-1] == True:
                print(f"{'': >6}Player {table.check_terminal_case(table.board)[0]} won!\n")
                break
            if not table.is_full(table.board):
                print(f"{'': >6}It's a Draw!")
                break
            
            if input('Press any key to continue...').lower() == 'quit':
                break
                
        # Human vs Random_AI
        while menu.decision == 3:
            
            hooman_ai = Game()
            
            if hooman == 'O':
                table.mark_the_coord(table.board,hooman_ai.hooman(),player)
                player = menu.swap_player(player)
                print(f"{'': >4}Player '{player}' will be moving!")
                table.display_board(table.board)
            hooman = 'O'    
            
            if table.check_terminal_case(table.board)[-1] == True:
                print(f"{'': >6}Player {table.check_terminal_case(table.board)[0]} won!\n")
                break
            if  not table.is_full(table.board):
                print(f"{'': >6}It's a Draw!")
                break
            
            
            table.mark_the_coord(table.board,hooman_ai.random_ai(),player)
            player = menu.swap_player(player)
            print(f"{'': >4}Player '{player}' will be moving!")
            table.display_board(table.board)

            
            if table.check_terminal_case(table.board)[-1] == True:
                print(f"{'': >6}Player {table.check_terminal_case(table.board)[0]} won!\n")
                break   
            if  not table.is_full(table.board):
                break
            
        # Human vs Unbeatable_AI
        while menu.decision == 4:
            
            hooman_uai = Game()
            if hooman == 'O':       
                table.mark_the_coord(table.board,hooman_uai.hooman(),player)
                player = menu.swap_player(player)
                print(f"{'': >4}Player '{player}' will be moving!")
                table.display_board(table.board)
            hooman = 'O' 
             
            if table.check_terminal_case(table.board)[-1] == True:
                print(f"{'': >6}Player {table.check_terminal_case(table.board)[0]} won!\n")
                break   
            if  not table.is_full(table.board):
                print(f"{'': >6}It's a Draw!")
                break
            
            
            if player == 'X':
                
                table.mark_the_coord(table.board,hooman_uai.unbeatable_ai_x_maximize(table.board)[1],player)
                player = menu.swap_player(player)
                print(f"{'': >4}Player '{player}' will be moving!")
                table.display_board(table.board)
            else:
                table.mark_the_coord(table.board,hooman_uai.unbeatable_ai_o_maximize(table.board)[1],player)
                player = menu.swap_player(player)
                print(f"{'': >4}Player '{player}' will be moving!")
                table.display_board(table.board)
            
            
            if table.check_terminal_case(table.board)[-1] == True:
                print(f"{'': >6}Player {table.check_terminal_case(table.board)[0]} won!\n")
                break   
            if  not table.is_full(table.board):
                print(f"{'': >6}It's a Draw!")
                break
            
        another_game = input("Do you want to play again? (y/n)")

        if another_game.lower() == 'y':
            os.system('cls')
            table.get_empty_board()
            continue
        
        else:
            print('Goodbye! o/\n')
            break

