from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    global data
    if by_values:
        order = {letter: num for num, letter in enumerate(data.keys())}
        data = OrderedDict(sorted(ordered_dict.items(), key=lambda x: (x[1], order[x[0]])))
    else:
        data = OrderedDict(sorted(ordered_dict.items()))
