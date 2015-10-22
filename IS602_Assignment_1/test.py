__author__ = 'jim'


def searchwithoutloops(input, value):

    return value in input

if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]

    print searchwithoutloops(L, 5) #true
    print searchwithoutloops(L, 11) #false
