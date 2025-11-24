import random
max = int(input("Enter upper limit:"))
num = random.randint(0, max)
guess = int(input("Guess the number:"))
count = 0
while guess != num:
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    count += 1
    guess = int(input("Guess the number:"))
if count == 1:
    print("Correct! The number is", num, "! You guessed it in a single try!")
elif count > 1:
    print("Correct! The number is", num, "! You guessed it in", count, "tries!")
