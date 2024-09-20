import sys

def main():
    try:
        old = input("Where would you like to start? ")
        old = int(old)
        while True:
            expression = input("Next Part: ")
            #print(interpreter(expression))
            opperation = expression[0]
            number = expression[1:]
            number = int(number)
            if opperation == "+":
                old += number
            elif opperation == "-":
                old -= number
            elif opperation == "/":
                old = old/number
            elif opperation == "x" or opperation == "*":
                old = old*number
            print(old)
    except:
        sys.exit("An error has been detected")
    
    

main()