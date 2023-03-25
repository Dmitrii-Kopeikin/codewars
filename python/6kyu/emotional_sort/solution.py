def sort_emotions(arr, order):
    if arr is False:
        return r'¯\_( ツ )_/¯'

    emotions_in_order = [':D', ':)', ':|', ':(', 'T_T']

    def get_index(element):
        return emotions_in_order.index(element)

    sorted_arr = list(arr)
    sorted_arr.sort(key=get_index)

    if order is False:
        sorted_arr.reverse()

    return sorted_arr
