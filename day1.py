
with open('day1_input', 'r') as input_data:
    numbers = [int(number.replace('\n', "")) for number in input_data]

numbers.sort()

for n1 in reversed(numbers):
    i = 0
    while n1 + numbers[i] <= 2020:
        i = i + 1
    if n1 + numbers[i - 1] == 2020:
        print(n1 * numbers[i - 1])
        break
