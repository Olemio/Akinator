import random
from pokemonDB import typeList


userPokemon = {}

#Maximum amount of Akinator questions 
allowedQuestions = 15

def getRandomType():
    return random.choice(typeList)

def type2Guess():
    pokemonType = getRandomType()

def type1Guess():
    pokemonType = getRandomType()  
    guessType = input('\nIs your pokemon', pokemonType+'?')
    if guessType == 'y':
        print('So your Pokemon is', pokemonType + '. Interesting.')
        type1 = pokemonType


def typeGuess():
    pokemonType = getRandomType()  
    typeGuess = input('\n\nIs your pokemon', pokemonType+'?')
    if typeGuess == 'y':
        print('So your Pokemon is', pokemonType + '. Interesting.')
        type = pokemonType
    else:
        return typeGuess()

def typingGuess():
    for i in range(allowedQuestions):  
        multiType = input('Does your Pokemon have more than one type?\n [y] or [n]?')
        if multiType == 'y':
            multiType = True
            type1Guess()
        elif multiType == 'n':
            print('\nYour Pokemon is only one type okay.')
            typeGuess()
        elif multiType != 'y' or 'n':
            print('Invalid input, please try again.')
            return typeGuess()

def intro():
    print('\nWelcome to "Akinator"')
    print('\nI will try to guess which pokemon you are thinking off based of some questions i will ask you')
    print('\nWith every question you will answer either y or n to either confirm or deny the question')
    introChoice()

def introChoice():
    startQ = input('\nAre you ready to play?\nPress [y] then ENTER to play the game\n').lower()
    if startQ == 'y':
        typingGuess()
    else:
        print('Incorrect input. Please try again')
        introChoice()

#Starts the game
if __name__ == "__main__":
    intro()
