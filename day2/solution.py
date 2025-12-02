input = open("input.txt", "r")

def palyndrom(s):
    if len(s)%2 == 1:
        return False
    firstHalf = s[:len(s)//2]
    secondHalf = s[len(s)//2:]
    return firstHalf == secondHalf

counter = 0
sets = input.read().split(",")
for set in sets:
    for i in range(int(set.split("-")[0]), int(set.split("-")[1]) + 1):
        if palyndrom(str(i)):
            counter += int(i)

print(counter)
input.close()