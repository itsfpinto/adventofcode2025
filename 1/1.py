dir_list = []
amount_list = []

with open("input", "r") as file:
    for line in file:
        if line.strip():
            dir_list.append(line.strip()[0])
            amount_list.append(int(line[1:]))

pos = 50
number_of_zeros = 0

def loop (nr):
    return nr % 100

for i in range(len(amount_list)):
    if dir_list[i] == "R":
        dial_movement = amount_list[i]
        pos += dial_movement
        pos = loop(pos)
    if dir_list[i] == "L":
        dial_movement = amount_list[i]
        pos -= dial_movement
        pos = loop(pos)
    if pos == 0:
        number_of_zeros += 1

print(number_of_zeros)