# guessing game

secret_number = 7
guessed_correctly=False
print("Can you guess what the number is?")

for counter in range(1,6):
    guess = input("Your guess ")
    guess= int(guess)


    if secret_number == guess :
        # do this if true
        print("You guessed correctly")
        guessed_correctly = True
        break
    else:
        print("You guessed incorrectly - have another go")
        guessed_correctly= False

#end of for loop
if guessed_correctly:
    print("It took you "+ str(counter) + " goes.")
else:
    print("Bad luck have another game")

