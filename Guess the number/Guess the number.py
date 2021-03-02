print("Welcome to Guess The Number Game \n")
import random
i = random.randint(1,100)
chance=1

while True:

    num = int(input("Enter a number:"+"\n"))

    if num == i:
        print("Congradulation,You have guessed the number.")
        break

    elif chance==5:
        print("Game over.You could not guess the number in 5 chances")
        print("The number is ",i)
        break

    elif num>100:
        print("Invalid input:Enter a number from 0 to 100")

    elif num>i:
        print("Enter a smaller number than ",num)
        chance = chance + 1

    elif num<i:
        print("Enter a greater number than ",num)
        chance = chance + 1

