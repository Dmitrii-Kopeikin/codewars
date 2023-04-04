def snail(snail_map):
    x_len = len(snail_map[0])
    y_len = len(snail_map)

    total_cells = x_len * y_len

    result = []

    x = 0
    y = 0
    x_direction = 1
    y_direction = 1
    x_steps_left = x_len
    y_len -= 1
    y_steps_left = y_len - 1
    while len(result) < total_cells:
        if x_steps_left > 0:
            while x_steps_left > 0:
                result.append(snail_map[y][x])
                x += x_direction
                x_steps_left -= 1
            else:
                x_direction *= -1
                x += x_direction
                x_len -= 1
                y += y_direction
                y_steps_left = y_len
        elif y_steps_left > 0:
            while y_steps_left > 0:
                result.append(snail_map[y][x])
                y += y_direction
                y_steps_left -= 1
            else:
                y_direction *= -1
                y += y_direction
                y_len -= 1
                x += x_direction
                x_steps_left = x_len

    return result


if __name__ == '__main__':
    array = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print(snail(array))
