import timeit


setup = '''

import numpy as np
import copy
import random

L_list = random.sample(xrange(10000), 1000)
L_np_array = np.array(L_list)


##### SORT #####

def sortwithloops(input):
    for i in xrange(1, len(input)):
        for j in xrange(i, 0, -1):

            if input[j - 1] < input[j]:
                break
            input[j], input[j - 1] = input[j - 1], input[j]
    return input

def sortwithoutloops(input):
    return(sorted(input))


def sortwithnumpy(input):
    return(np.sort(input))


##### SEARCH #####

def searchwithloops(input):
    for i in range(0, len(input)):
        if input[i] == 3456:
            return True
    else:
        return False

def searchwithoutloops(input):
    return 3456 in input

def searchwithnumpy(input):
    return(np.where(3456))


'''



n = 100

print("Time to process %d loops:" % n)

t = timeit.Timer("x=copy.copy(L_list); sortwithloops(x)", setup=setup)
print("Sort without loops:", t.timeit(n))

t = timeit.Timer("x=copy.copy(L_list); sortwithoutloops(x)", setup=setup)
print("Sort without loops:", t.timeit(n))

t = timeit.Timer("x=copy.copy(L_np_array); sortwithnumpy(x)", setup=setup)
print("Sort with numpy:", t.timeit(n))

######

t = timeit.Timer("x=copy.copy(L_list); searchwithloops(x)", setup=setup)
print("Search with loops:", t.timeit(n))

t = timeit.Timer("x=copy.copy(L_list); searchwithoutloops(x)", setup=setup)
print("Search without loops:", t.timeit(n))

t = timeit.Timer("x=copy.copy(L_list); searchwithnumpy(x)", setup=setup)
print("Search with numpy:", t.timeit(n))