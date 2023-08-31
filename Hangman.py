import random

def hangman(): # define the game/function
    wrong = 0 # set list for number of answers
    stages = ["",
              "_________         ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",    # Create the 'hangman' - named stages. In the format of a list 
              "|        |        ",
              "|       / \       ",
              "|                 "
              ]
    
    words = ["Dog", "Cat", "Monkey", "Chair", "Steak", "Rhino"] #creating list fo words to random.choice form
    word = random.choice(words) # calling random.choice

    rletters = list(word) #Turning the word into a list of characters
    board = ["__"] * len(rletters) #Creating the "board" of dashes to represent each letter in the word
    win = False #setting the win status
    print("Welcome to Hangman") # welcome message
    while wrong < len(stages) -1: #As long as the wrong answers is less than the stages the player can continue (-1 to represent index)
        print("\n") # newline not sure why
        msg = "Guess a letter" # setting the input message to a variable
        char = input(msg) #assinging the input variable to the messagd
        if char in rletters: #checking if the guessed character is in the list of characters from the word
            cind = rletters.index(char) # creating a variable for the index of the correctly guessed character 
            board[cind] = char #representing this on the baord as well as the hidden word - reveasl that word
            rletters[cind] = "$"  #changing the letter in the word so no repeat of letter
        else: #else statement for the wrong answer
            wrong += 1 # if wrong answer the wrong variable has 1 added
        print((" ".join(board))) #prints the unchanged board
        e = wrong + 1 #represents the index of the stage got to on the hanging man assigned toa variable
        print("\n".join(stages[0: e])) # prints the hang man, each stage on a new line from the first index to the length of wrong guesses
        if "__" not in board: # if statement to print win if all letters guessed
            print("You Win!") #win print statement
            print(" ".join(board)) # prints the new board
            win = True #set win to true
            
            break # break statement
    if not win: # if statement if not win
        print("\n".join(stages[0: wrong])) #print the hangman image using slicing
        print("you lose! it was {}.".format(word)) #print the loss statement and show the word

hangman()