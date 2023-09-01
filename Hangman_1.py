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
    
    words = ["Dog", "Cat", "Monkey", "Chair", "Steak", "Rhino"] 
    word = random.choice(words) 

    rletters = list(word)
    board = ["__"] * len(rletters) 
    win = False 
    print("Welcome to Hangman") 
    while wrong < len(stages) -1: 
        print("\n") 
        msg = "Guess a letter" 
        char = input(msg) 
        if char in rletters: 
            cind = rletters.index(char) 
            board[cind] = char 
            rletters[cind] = "$"  
        else: 
            wrong += 1 
        print((" ".join(board))) 
        e = wrong + 1 
        print("\n".join(stages[0: e])) 
        if "__" not in board: 
            print("You Win!") 
            print(" ".join(board)) 
            win = True
            
            break 
    if not win: 
        print("\n".join(stages[0: wrong])) #
        print("you lose! it was {}.".format(word)) 

hangman()