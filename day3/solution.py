def max_joltage(bank):
    battery1 = 0
    battery2 = 0
    index = 0

    for i in range(len(bank)-1):
        if int(bank[i]) > battery1:
            battery1 = int(bank[i])
            index = i
    
    for i in range(index+1, len(bank)):
        if int(bank[i]) > battery2:
            battery2 = int(bank[i])
    
    joltage = str(battery1) + str(battery2)

    return int(joltage)

input = open("input.txt", "r")
total_joltage = 0

banks = input.read().split()

for bank in banks:
    total_joltage += max_joltage(bank)

print(total_joltage)
input.close()