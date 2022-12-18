class Menu:
    
    def __init__(self,decision = None,player = 'X'):
        self.decision = decision
        self.player = player
    
        # Pop ups main menu where player can choose his game
    def show_menu(self):
        print('''
    Welcome in Tic Tac Toe Game, what would u like to play? 

    1. Human vs Human
    2. Random AI vs Random AI
    3. Human vs Random AI
    4. Human vs Unbeatable AI 
            ''') 
        while True:
            
            self.decision = input('What is your choice? ')
            if self.decision.lower() == 'quit':
                quit()    
            try:
                self.decision = int(self.decision)
            except ValueError:
                print("I don't recognize that option, please try again...")
                continue
            if self.decision not in range(1,5):
                print("I don't recognize that option, please try again...")
                continue
            return self.decision
        
        # Asks a player if he want to play first or not
    def starting_player(self,player):
        
        if self.decision != 2:
        
            while True:
                player = input('Would you like to start first? (y/n)')
                
                if player.lower() == 'y':
                    print('You are starting 1st as an O')
                    return 'O'
                
                if player.lower() == 'n':
                    print('You are starting 2nd as an X')
                    return 'X'
                
                if player == 'quit':
                    quit()
                    
                else:
                    print("I don't know what u mean by that...")
        
        return 'O'
    
        # Swap a player to another 
    def swap_player(self,player):
        
        if player == 'X':
            return 'O'
        else:
            return 'X' 