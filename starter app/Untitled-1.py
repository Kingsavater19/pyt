who_am_i="Y"
guess=""
limit=3
outofguess=False
count=0
print("i have a tail and two branches. \n WHO  AM I ?")
while (who_am_i != guess) and not outofguess:
    if count < limit:
        guess= input("Who i am ? : ").capitalize()
        count += 1
    else:
        outofguess=True
if outofguess:
    print("out of guess, you have lose")
else:
    print("you win")
