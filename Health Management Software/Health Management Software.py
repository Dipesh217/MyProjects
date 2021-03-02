def getdate():
    import datetime
    return  datetime.datetime.now()
def Dipesh_Log():
        print("")
        print("Enter 1 - Log Excersise" + "\n" + "Enter 2 - Log Diet")
        c = int(input("Enter your Choice:"))
        if c==1:
            print("")
            Excersise = input("Enter the Excersise:")
            with open("Dipesh.Ex","a") as f:
                f.write(str(getdate())+ ": " + Excersise + "\n")
                print("Noted Sucessfully!")

        elif c==2:
            print("")
            Diet = input("Enter the Diet Food:")
            with open("Dipesh.Diet", "a") as f:
                f.write(str(getdate())+ ": " + Diet + "\n")
                print("Noted Sucessfully!")
        else:
            print("")
            print("Check The Input!!")

def Dipesh_Retreive():
        print("")
        print("Enter 1 -Retreive Excersise" + "\n" + "Enter 2 - Retreive Diet")
        c = int(input("Enter your Choice:"))
        if c == 1:
            print("")
            with open("Dipesh.Ex","r") as f:
                print(f.read())
        elif c == 2:
            print("")
            with open("Dipesh.Diet","r") as f:
                print(f.read())

def Chirag_Retreive():
        print("")
        print("Enter 1 -Retreive Excersise" + "\n" + "Enter 2 - Retreive Diet")
        c = int(input("Enter your Choice:"))
        if c == 1:
            with open("Chirag.Ex", "r") as f:
                print(f.read())
        elif c == 2:
            with open("Chirag.Diet", "r") as f:
                print(f.read())

def Divyanshu_Retreive():
            print("")
            print("Enter 1 -Retreive Excersise" + "\n" + "Enter 2 - Retreive Diet")
            c = int(input("Enter your Choice:"))
            if c == 1:
                with open("Divyanshu.Ex", "r") as f:
                    print(f.read())
            elif c == 2:
                with open("Divyanshu.diet", "r") as f:
                    print(f.read())

def Chirag_Log():
    while True:
        print("")
        print("Enter 1 - Log Excersise" + "\n" + "Enter 2 - Log Diet")
        c = int(input("Enter your Choice:"))
        if c == 1:
            Excersise = input("Enter the Excersise:")
            with open("Chirag.Ex", "a") as f:
                f.write(str(getdate())+ ": " + Excersise + "\n")
                print("Noted Sucessfully!")

        elif c == 2:
            Diet = input("Enter the Diet Food:")
            with open("Chirag.Diet", "a") as f:
                f.write(str(getdate())+ ": " + Diet + "\n")
                print("Noted Sucessfully!")
        else:
            print("Check The Input!!")

def Divyanshu_Log():
        print("")
        print("Enter 1 - Log Excersise" + "\n" + "Enter 2 - Log Diet")
        c = int(input("Enter your Choice:"))
        if c == 1:
            Excersise = input("Enter the Excersise:")
            with open("Divyanshu.Ex", "a") as f:
                f.write(str(getdate())+ ": " + Excersise + "\n")
                print("Noted Sucessfully!")

        elif c == 2:
            Diet = input("Enter the Diet Food:")
            with open("Divyanshu.diet", "a") as f:
                f.write(str(getdate())+ ": " + Diet + "\n")
                print("Noted Sucessfully!")
        else:
            print("Check The Input!!")

def log():
        print("")
        print("Enter 1- Dipesh" + "\n" + "Enter 2- chirag"  "\n" + "Enter 3- Divyanshu")
        b = int(input("Enter your choice:"))
        if b==1:
            Dipesh_Log()
        elif b==2:
            Chirag_Log()
        elif b==3:
            Divyanshu_Log()
        else:
            print("Enter Correct Option!!")

def retreive():
        print("")
        print("Enter 1- Dipesh" + "\n" + "Enter 2- chirag"  "\n" + "Enter 3- Divyanshu")
        b = int(input("Enter your choice:"))
        if b == 1:
            Dipesh_Retreive()
        elif b==2:
            Chirag_Retreive()
        elif b==3:
            Divyanshu_Retreive()
        else:
            print("Check the Input!!")

if __name__ == '__main__':
        print("Welcome To Health Management System \n")
        print("Enter 1- Log" + "\n" + "Enter 2- Retreive")
        a = int(input("Enter your choice:"))
        if a == 1:
            log()
        elif a == 2:
            retreive()
        else:
            print("Check the Input!! \n")