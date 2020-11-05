def myreduce(func, lis):
    result = lis[0]
    for element in lis[1:]:
        result = func(result, element)
    return result
