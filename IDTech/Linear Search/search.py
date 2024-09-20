entries = [45, 34, 56, 88, 50, 87, 99, 12, 67, 29, 8, 33]
key = 88

def main():
    search(entries, key)

def search(entries, key):
    for i in range(len(entries)):
        if entries[i] == key:
            print("Submission", i+1, "was the correct submmision")
            break


main()