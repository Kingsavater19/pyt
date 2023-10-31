
secret_word="haaland"
guess=""
guess_count=0
guess_limit=3
guess_outofguess=False
print("I scored 30+ Goals, in the 2022-2023 Season.\n WHO AM I ?")
while (secret_word != guess) and not (guess_outofguess):
    if guess_count < guess_limit:
        guess=input("Enter guess : ").lower()
        guess_count +=1
    else :
        guess_outofguess=True
if guess_outofguess:
    print("Out of guesses, YOU LOSE !")
else:
    print("you win!")