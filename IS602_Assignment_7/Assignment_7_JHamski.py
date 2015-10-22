import timeit

from scipy import stats

import csv
with open('brainandbody.csv', 'rb') as f:
    data = list(csv.reader(f))

x = [float(i[1]) for i in data]
y = [float(i[2]) for i in data]


slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("The slope is %f and the intercept is %f.") % (slope, intercept)

setup = '''
import csv
with open('brainandbody.csv', 'rb') as f:
    data = list(csv.reader(f))
import copy


def LinearRegressionJim(data):
    x = [float(i[1]) for i in data]
    Xsum = sum(x)
    

    y = [float(i[2]) for i in data]
    Ysum = sum(y)


    numlist = [float(i[1])*float(i[2]) for i in data]
    XYsum = sum(numlist)


    Xmean = Xsum / len(data)

    Ymean = Ysum / len(data)

    XXbar = [float(i[1])-Xmean for i in data]
    XXbar_sum = sum(XXbar)

    YYbar = [float(i[2])-Ymean for i in data]
    YYbar_sum = sum(YYbar)

    slope_numerator = [((float(i[1])-Xmean) * (float(i[2])-Ymean)) for i in data]
    slope_numerator = sum(slope_numerator)

    slope_denominator = [((float(i[1])-Xmean)**2) for i in data]
    slope_denominator = sum(slope_denominator)

    slope_jim = slope_numerator / slope_denominator

    intercept_jim = Ymean - slope_jim*Xmean

    return(slope_jim, intercept_jim)


def LinearRegressionSciPy(data):
    from scipy import stats


    x = [float(i[1]) for i in data]
    y = [float(i[2]) for i in data]


    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    return(slope, intercept)


def Polynomial2(data):
    import numpy


    x = [float(i[1]) for i in data]
    y = [float(i[2]) for i in data]

    deg = 2

    z = numpy.polyfit(x, y, deg)

    return(z)

def Polynomial6(data):
    import numpy


    x = [float(i[1]) for i in data]
    y = [float(i[2]) for i in data]

    deg = 6

    z = numpy.polyfit(x, y, deg)

    return(z)

'''


n = 10000

print("Time to process %d loops:" % n)

t = timeit.Timer("x=copy.copy(data); LinearRegressionJim(x)", setup=setup)
print("Jim's linear regression script:", t.timeit(n))

t = timeit.Timer("x=copy.copy(data); LinearRegressionSciPy(x)", setup=setup)
print("SciPy linear regression method:", t.timeit(n))

t = timeit.Timer("x=copy.copy(data); Polynomial2(x)", setup=setup)
print("2nd degree polynomial method:", t.timeit(n))

t = timeit.Timer("x=copy.copy(data); Polynomial6(x)", setup=setup)
print("6nd degree polynomial  method:", t.timeit(n))