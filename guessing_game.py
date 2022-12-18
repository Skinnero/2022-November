import math
import random

GAME_TURNS = 10
MIN = 1
FIRST_MAX = 99
SECOND_MAX = 49
def random_choices(min,max,game_turns):
    choices_list = [random.randint(min,max) for num in range(game_turns)]
    return choices_list

def ask_for_number(choice,min,max):
    for i in range(len(choice)):
        guess = None
        while choice[i] != guess:
            guess = int(input(f"Enter an integer from {min} to {max}: "))
            if guess < choice[i]:
                print("guess is low") 
            else:
                print("guess is high")
        print("you guessed it!")
def main():       
    choices_1 = random_choices(MIN,FIRST_MAX,GAME_TURNS) 
    ask_for_number(choices_1,MIN,FIRST_MAX)       
    choices_2 = random_choices(MIN,SECOND_MAX,GAME_TURNS)
    ask_for_number(choices_2,MIN,SECOND_MAX)

if __name__ == '__main__':
    main()