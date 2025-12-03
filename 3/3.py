import os
def day3_part1():
    banks = []

    try:
        with open("/Users/ctw00416/adventofcode2025/adventofcode2025/3/input", 'r') as file:
            content = file.read()
            banks = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '/Users/ctw00416/adventofcode2025/adventofcode2025/3/input' was not found.")
 
    sum = 0

    for bank in banks:
        largest = get_largest_two(bank)
        sum += largest

    print(sum)

def get_largest_two(value):
    first = value[0]
    second = value[1]

    for i in range(1, len(value)-1):
        if value[i] > first:
            first = value[i]
            second = value[i+1]
        elif value[i] > second:
            second = value[i]
    
    if value[-1] > second:
        second = value[-1]

    final = int(first)*10 + int(second)
    return final

result = day3_part1()
print(result)