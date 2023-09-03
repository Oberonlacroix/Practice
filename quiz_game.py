

print("Welcome to th equiz game")

playing = input("Would you like to play? Y/N: ")

if playing.lower() != 'y':
    quit()

print("Okay lets play!")
score = 0

answer = input("What sport is the best? ")
if answer.lower() == "basketball":
    print("Well done!")
    score += 1
else:
    print("Incorrect answer, it is Basketball! of course")

answer_2 = input("What country is london the capital city of? ")
if answer_2.lower() == "england":
    print("Well done!")
    score += 1
else:
    print("Incorrect answer, it is England")

answer_3 = input("What colour is grass?")
if answer_3.lower() == "green":
    print("Well done!")
    score += 1
else:
    print("Incorect answer")


print("Your final score was", score)
print("Your percentage was", (score / 3) * 100, "% ")