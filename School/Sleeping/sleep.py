isSleeping = False

while True:
    name = input("What's Your Name? ")
    if name == "Mr. Scimeca":
        print("Hi!")
        continue
    
userNum = int(input("How many hours did you sleep last night? "))

if isSleeping:
    print("Wake Up")
elif userNum >=8:
    print("Good Morning")
else:
    print("You shoudl get more sleep")

print(" - Program End - ")