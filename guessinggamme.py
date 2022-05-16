print("i am the beginning the middle and end, time respects me and nothing escapes my grasp") 
secret_word = "bem"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:
    guess = input("Guess the secret word!: ")
    guess_count += 1
    if guess_count > guess_limit:
        out_of_guesses = True
        break

if out_of_guesses:
    print("Out of Guesses, You fucking Donkey!")
else:
    print("You got it! It took you " + str(guess_count) + " guesses!")
guess_count = 0
  