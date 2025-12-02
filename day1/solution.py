input = open("input.txt", "r")

starting_point = 50
password = 0

for line in input:
    line = line.strip()

    if not line:
        continue

    rotation = line[0]
    steps = line[1:]
    steps = int(steps)

    if rotation == "R":
        starting_point = (starting_point + steps) % 100
    elif rotation == "L":
        starting_point = (starting_point - steps) % 100
    
    if starting_point == 0:
        password += 1

print(password)
input.close()