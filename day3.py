
cords = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(x_step, y_step):
    input_data = open('day3_input', 'r')

    count = 0
    y_pos = 0
    line_length = 0
    i = 1
    while True:
        line = input_data.readline()
        line = line.replace('\n', "")
        if not line:
            break

        if y_pos == 0 or y_pos % y_step != 0:  # skip the first line
            line_length = len(line)
            y_pos = y_pos + 1
            continue

        x_pos = (x_step * i) % line_length
        if line[x_pos] == '#':
            count = count + 1
        y_pos = y_pos + 1
        i = i + 1

    input_data.close()
    return count


total = 1
for c in cords:
    result = count_trees(c[0], c[1])
    total = total * result
    print(f"results: {result}")

print(total)
