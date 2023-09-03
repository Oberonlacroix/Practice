name = input("Write your name: ")
print("Welcome " + name + " this is your adventure")


answer = input("You come to a dirt road would you like to go right or left? ")

if answer.lower() == "left":
    answer = input("You walk further down to the left and find yourself a pot of gold, do you take it? Y/N ")
    if answer.lower() == 'y':
        answer = input("You start to walk off with the gold, but hear footsteps approaching from behind, do you run or hide? ")
        if answer.lower() == "hide":
             print("you jump in the bush and fall asleep")
        elif answer.lower() == "run":
            print("You run trip and bahs your head open")
        else:
            print("you didn't choose left or right, you lose!")
    elif answer.lower() == "n":
        print("You left the gold and starved to death because you couldn't afford any food ")
elif answer.lower() == "right":
    print("You went right and passed out")
else:
    print("Incorrect answer, you lose!")

print("Thank you for your efforts, but your adventure is over")        
