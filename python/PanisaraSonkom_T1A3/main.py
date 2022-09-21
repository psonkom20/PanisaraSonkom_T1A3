#import random package to enable randomise character function
#import cowsay to add graphic
#import character list from character file
import random
import cowsay
from character import charList

#Main menu
#instruction of game
#implement 'ready' so that user can enter the game
user_command = ''
cowsay.dragon("Are you ready to fight for the throne?!! This game is simple, but a word of warning, do not underestimate it. Player who dare plays your task is simple. You will be given a quote and all you have to do is enter the name of the character who said the quote. IMPORTANT: You must write the character full name to pass. For each round you will have 20 seconds to guess. You will also have 2 chances to guess for each round. If you are stuck type 'hint' to receive a clue. But use it carefully as there are only 3 hints available for the entire game. To win you must pass all 10 rounds. Goodluck!")
user_command = print(input("If you are ready enter 'ready': "))
#code to randomly generate a character from any dictionary
chosen_character = charList[random.randint(0,14)]



#Main game set up
#Add 'quit' to let user quit at anytime
#Implement 'hint' function to allow user access to clue; limit: 3 hints
round_count = 0
guess_count = 0

while round_count < 10:
    if guess_count == 0:
        cowsay.dragon(chosen_character['Quote'])
        answer = print(input("Which character said this?: "))
        guess_count += 1
        if answer != chosen_character['Name'] and guess_count < 2:
            answer = print(input("Try again! Which character said this? You have one chance left: "))
            guess_count += 1
            if answer == chosen_character['Name']:
                print("You are correct")
                guess_count += 1
            else:
                cowsay.dragon('Game over: You loss your chance to fight for the Throne')
        elif answer == chosen_character['Name']:
            print("You are correct!")
            round_count += 1
        
        else:
            cowsay.dragon('Game over: You loss your chance to fight for the Throne')
            break
    
   

