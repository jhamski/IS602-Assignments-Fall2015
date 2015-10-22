
# coding: utf-8

## Homework #5 - Advanced Programming Techniquest - James Hamski

# 1) Download the new data set on the Lesson 5 page called brainandbody.csv.  This file is a small set of average brain weights and average body weights for a number of animals.  We want to see if a relationship exists between the two. (This data set acquired from here).
# 2) Perform a linear regression using the least squares method on the relationship of brain weight [br] to body weight [bo].  Do this using just the built in Python functions (this is really easy using scipy, but we're not there yet).  We are looking for a model in the form bo = X * br + Y.  Find values for X and Y and print out the entire model to the console.

# In[23]:

import csv
with open('brainandbody.csv', 'rb') as f:
    data = list(csv.reader(f))


# ['animal', 'body', 'brain']

# In[24]:

data[0]


# Let Body be the independent variable X and Brain be the dependent variable Y. 
# 
# The sum of X is:

# In[55]:

numlist = [float(i[1]) for i in data]
Xsum = sum(numlist)
print(Xsum)


# The sum of Y is:

# In[56]:

numlist = [float(i[2]) for i in data]
Ysum = sum(numlist)
print(Ysum)


# The sum of XY is:

# In[57]:

numlist = [float(i[1])*float(i[2]) for i in data]
XYsum = sum(numlist)
print(XYsum)


# The mean of X is:

# In[61]:

Xmean = Xsum / len(data)
print(Xmean)


# The mean of Y is:

# In[63]:

Ymean = Ysum / len(data)
print(Ymean)


# Finding the slope:

# In[66]:

XXbar = [float(i[1])-Xmean for i in data]
XXbar_sum = sum(XXbar)


# In[67]:

YYbar = [float(i[2])-Ymean for i in data]
YYbar_sum = sum(YYbar)


# In[71]:

slope_numerator = [((float(i[1])-Xmean) * (float(i[2])-Ymean)) for i in data]
slope_numerator = sum(slope_numerator)
print(slope_numerator)


# In[72]:

slope_denominator = [((float(i[1])-Xmean)**2) for i in data]
slope_denominator = sum(slope_denominator)
print(slope_denominator)


# In[76]:

slope = slope_numerator / slope_denominator
print(slope)


# The b intercept is:

# In[77]:

b_intercept = Ymean - slope*Xmean
print(b_intercept)


# The resulting linear model is:

# $$bo = 0.966br + 91$$

print("bo = %fbr + %f" % (slope, b_intercept))
