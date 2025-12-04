input = open("input.txt", "r")
grid = input.readlines()

def check_position (position, i, j):
    num_of_roll = 0
    if(i != 0 and j != 0 and position[i - 1][j - 1] == "@"):
        num_of_roll += 1
    if(i != 0 and position[i - 1][j] == "@"):
        num_of_roll += 1
    if(i != 0 and j != len(position[i]) and position[i - 1][j + 1] == "@"):
        num_of_roll += 1
    if(j != 0 and position[i][j - 1] == "@"):
        num_of_roll += 1
    if(j != len(position[i]) and position[i][j + 1] == "@"):
        num_of_roll += 1
    if(j != 0 and i != (len(position) - 1) and position[i + 1][j - 1] == "@"):
        num_of_roll += 1
    if(i != (len(position) - 1) and position[i + 1][j] == "@"):
        num_of_roll += 1
    if(j != len(position[i]) and i != (len(position) - 1) and position[i + 1][j + 1] == "@"):
        num_of_roll += 1
    
    return (num_of_roll < 4)

accessable_roll = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if(grid[i][j] == "@" and check_position(grid, i, j)):
            accessable_roll += 1

print(accessable_roll)