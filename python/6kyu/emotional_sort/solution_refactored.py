def sort_emotions(arr, order):
    emotions_in_order = [':D', ':)', ':|', ':(', 'T_T']

    return sorted(arr, key=emotions_in_order.index, reverse=(not order))
