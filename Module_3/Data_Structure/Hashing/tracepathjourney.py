


def trace_path(my_dict):
    result = []
    dict_keys = my_dict.keys()
    reverse_dict = dict()
    for key in dict_keys:
        reverse_dict[my_dict.get(key)] = key
    from_loc = None
    reverse_keys = reverse_dict.keys()
    for key in dict_keys:
        if key not in reverse_dict:
            from_loc = key
            break
    to = my_dict.get(from_loc)
    while to is not None:
        result.append[from_loc, to]
        from_loc = to 
        to = my_dict.get(to)
    return result
