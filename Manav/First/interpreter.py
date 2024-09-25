arr = []
chars = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\"', '\'', '+', '-', '/', '*', '/', '%', '^', '<', '>', ':', '!', '@', '#', '$', '&', ';', '    ', '\n']
output = ""
with open("codeBin.txt", "r") as file:
    for line in file:
        line = line.strip()
        #line = line.replace("pranav", "1")
        #line = line.replace("mano", "0")
        line = int(line, 2)
        arr.append(line)



for i in arr:
    i = i%len(chars)
    output += chars[i]

print(output)