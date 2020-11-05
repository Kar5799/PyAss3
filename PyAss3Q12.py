def myfilter(func, lis):
    new_list = []
    for element in lis:
        if func(element):
            new_list.append(element)
    return iter(new_list)