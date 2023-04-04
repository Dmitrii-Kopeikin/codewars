def snail(snail_map: list[list]):
    result = []
    while len(snail_map) > 0:
        result += snail_map.pop(0)
        snail_map = list(zip(*snail_map))[::-1]

    return result


if __name__ == '__main__':
    array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(snail(array))
