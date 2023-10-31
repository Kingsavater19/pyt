is_male=False
is_tall=False

if is_male  or is_tall:
    print("you are a male or tall or both")
else:
    print("you are not a male but your tall")
print("----------------")
if is_male and is_tall:
    print("your are a tall and a male")
else:
    print("your either not a male or not tall")
print("----------------")
if is_male  and is_tall:
    print("you are a male or tall or both")
elif is_tall and not is_male:
    print("you are tall but not a male")
elif is_male and not is_tall:
    print("you are male but you are not tall")
else:
    print("you are not a male and  you are not tall")