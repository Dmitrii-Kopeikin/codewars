from collections import OrderedDict


def get_unit_str(count: int, time_unit: str) -> str:
    if count == 0:
        return ""
    return f"{count} {time_unit}{'s' if count > 1 else ''}"


def format_duration(seconds: int) -> str:
    if seconds < 0:
        raise ValueError

    if seconds == 0:
        return 'now'

    my_dict = OrderedDict()
    my_dict["year"] = int(seconds / (60 * 60 * 24 * 365))
    seconds = seconds % (60 * 60 * 24 * 365)
    my_dict["day"] = int(seconds / (60 * 60 * 24))
    seconds = seconds % (60 * 60 * 24)
    my_dict["hour"] = int(seconds / (60 * 60))
    seconds = seconds % (60 * 60)
    my_dict["minute"] = int(seconds / 60)
    my_dict["second"] = seconds % 60

    tmp_list = []
    for time_unit, count in my_dict.items():
        if count > 0:
            tmp_list.append(get_unit_str(count, time_unit))

    if len(tmp_list) == 1:
        return tmp_list[0]

    return " and ".join([", ".join(tmp_list[0:-1]), tmp_list[-1]])


if __name__ == '__main__':
    # generator = union_str_generator(3)
    # for _ in generator:
    #     print(_)

    print(format_duration(2))
