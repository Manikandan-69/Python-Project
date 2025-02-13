import random
n=random.randrange(1,10)
print("Enter number between 1 and 10")
guess=int(input("Enter any number: "))
while guess!=n:
    if guess < n:
        print("Too small")
        guess=int(input("Enter any number: "))
    elif guess > n:
        print("Too high")
        guess=int(input("Enter any number: "))
    else:
        break
print("You guessed it Right!!!!")
