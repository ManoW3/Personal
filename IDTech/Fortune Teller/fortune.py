import random

def main():
    rand = random.randint(1, 10)
    teller(rand)

def teller(rand):
    print("YOu got the number ", rand)
    if rand <=4:
        print("Bad Fortune")
    elif rand >= 8:
        print("Good Fortune")
    else:
        print("Mid Fortune")


main()