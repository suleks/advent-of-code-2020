
with open('day1_input', 'r') as input_data:
    numbers = [int(number.replace('\n', "")) for number in input_data]

numbers.sort()

# part 1
for n1 in reversed(numbers):
    i = 0
    while n1 + numbers[i] <= 2020:
        i = i + 1
    if n1 + numbers[i - 1] == 2020:
        print(n1 * numbers[i - 1])
        break

# part 2
found = False
for n1 in reversed(numbers):
    i = 0
    while not found and i < len(numbers):
        j = 0
        while n1 + numbers[i] + numbers[j] <= 2020:
            if n1 + numbers[i] + numbers[j] == 2020:
                found = True
                break
            j = j + 1
        i = i + 1

    if n1 + numbers[i-1] + numbers[j] == 2020:
        print(n1 * numbers[i-1] * numbers[j])
        break
