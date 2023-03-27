def move_zeros(lst):
    zero_indexes = []
    for index in range(len(lst)):
        if lst[index] == 0:
            zero_indexes.append(index)
        elif len(zero_indexes):
            lst[index], lst[zero_indexes[0]] = lst[zero_indexes[0]], lst[index]
            zero_indexes.pop(0)
            zero_indexes.append(index)

    return lst


if __name__ == '__main__':
    pass
