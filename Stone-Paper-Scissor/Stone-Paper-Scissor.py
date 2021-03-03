import random

print("Welcome To " +"\n" + "Stone-Paper-Scissor \n")


while True:
    a = ["Stone", "Paper", "Scissor"]
    b = random.choice(a)
    print(b)
    Choice = input("Enter Your Choice:")

    if b==Choice:
        print("Its a tie")

    elif b=="Stone":
        if Choice=="Paper":
            print("You win")

        elif Choice=="Scissor":
            print("You Lose")

        else:
            print("Check The Input!!")

    elif b=="Paper":
        if Choice=="Stone":
            print("You lose")

        elif Choice=="Scissor":
            print("You Win")

        else:
            print("Check The Input!!")

    elif b=="Scissor":
        if Choice=="Stone":
            print("You Win")

        elif Choice=="Paper":
            print("You Lose")

        else:
            print("Check The Input!!")



