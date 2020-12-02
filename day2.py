
with open('day2_input', 'r') as input_data:
    lines = input_data.readlines()

# part 1
counter = 0
for line in lines:
    line = line.replace("\n", "")

    (key_range, key, password) = line.split(" ")
    key = key.replace(":", "")

    counted_letters = password.count(key)

    (min, max) = key_range.split("-")

    is_in_range = int(min) <= counted_letters <= int(max)

    if is_in_range:
        counter = counter + 1

print(f"part 1 solution: {counter}")

# part 2
counter_2 = 0
for line in lines:
    line = line.replace("\n", "")

    (key_range, key, password) = line.split(" ")
    key = key.replace(":", "")

    (ps_1, ps_2) = key_range.split("-")

    is_at_index = (password[int(ps_1) - 1] == key) != (password[int(ps_2) - 1] == key)
    if is_at_index:
        counter_2 = counter_2 + 1

print(f"part 2 solution: {counter_2}")
