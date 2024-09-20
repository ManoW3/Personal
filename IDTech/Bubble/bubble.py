import random
from datetime import datetime
startTime = datetime.now()

entries = []


def main():
    totalSwaps = 0
    totalRuns = 10000
    for _ in range(totalRuns):
        for i in range(25):
            entries.append(random.randint(1,100))
        totalSwaps = bubble(entries)
    print("In", totalRuns, "Runs,", totalSwaps,"swaps were made. This is an average of", round(totalSwaps/totalRuns, 3), "swaps per run")


def bubble(entries):
    timeA = datetime.now()
    temp = 0
    counter = 0
    for i in range(len(entries)):
        swapped = False
        for j in range(len(entries)-i-1):
            if entries[j] > entries[j+1]:
                #print(entries)
                counter+=1
                temp = entries[j]
                entries[j] = entries[j+1]
                entries[j+1] = temp
                swapped = True
        if swapped == False:
            break
    print("This array took: ", datetime.now()-timeA)
    return counter

main()
print("The program took", datetime.now() - startTime)