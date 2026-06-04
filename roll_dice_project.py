import random

while(True):
    option = input("Roll the dice?(y/n):")
    if option.lower() == "y" :
        t = (random.randint(1,6),random.randint(1,6))
        print(t)
    elif option.lower() == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid Choice!!")
        continue



    