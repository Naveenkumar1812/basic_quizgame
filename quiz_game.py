print("Welcome to my computer quiz!")
print("DISCLAIMER: should use lowercase letters for answers")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("where tajmahal is located? ")
if answer == "agra":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("who calles as thala in cricket? ")
if answer == "dhoni":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is the capital of bangladesh? ")
if answer == "dhaka":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("Your score is " + str((score / 3) * 100) + "%.")