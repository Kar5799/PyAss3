l1 = [var*i for var in ['x', 'y', 'z'] for i in [1, 2, 3]]
l2 = [var*i for i in [1, 2, 3] for var in ['x', 'y', 'z']]
l3 = [[var+i] for i in [0, 1, 2] for var in [2, 3, 4]]
l4 = [[var+i for i in [0, 1, 2, 3]] for var in [2, 3, 4, 5]]
l5 = [(i, j) for j in [1, 2, 3] for i in [1, 2, 3]]
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)