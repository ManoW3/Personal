import time
import random
import os

def main():
    cur = ""
    alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", ",", ".", "&", "@", "#", "$", "%", "^", "*", "-", "_", "+", "=", "?", "(", ";", ":", "?", "/"]

    word = input("What is your word/phrase? ")
    for i in range(len(word)):
        random.shuffle(alphabet)
        for j in range(len(alphabet)):
            time.sleep(0.01)
            letter = alphabet[j]
            cur += letter
            print(cur)
            if letter == word[i]:
                break
            else:
                cur = cur[:-1]
    os.system('cls' if os.name == 'nt' else 'clear')
    print(word)
main()