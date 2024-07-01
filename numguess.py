import random
upper=int(input())
lower=int(input())
num=random.randint(upper,lower)
chances=5
count=0
print("You have only 5 chances use them wisely ;)")
while count<chances:
    count+=1
    guess=int(input())
    if guess==num:
       print("You have guessed right!")
       break
    elif guess<num:
       print("Too low! Try again")
    elif guess>num:
       print("Too high! Try again")
    else:
        print("Try again :(")
if count>=chances:
    print("Oops! You are out of chances. The correct answer was "+ str(num))
        