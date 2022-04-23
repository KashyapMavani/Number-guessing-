import random

top_of_range = input("Type the top range of number : ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than zero next time.")
        quit()
else :
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0 

while True:

    guess_number = int(input("Guess the Number :"))
    if guess_number == random_number:
        print("You got it!")
        guesses +=1
        break
    else :
        print("Wrong guess try again.")

print("You guessed correct "+str(guesses)+" times.")