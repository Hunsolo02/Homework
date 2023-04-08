#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Задача №1
def share_bread(N, K):
    x= K//N
    y= K%N
    return x, y

#Задача №2
def leap_year(year):
    if year%4 == 0 and year%100 != 0 and year%400 == 0:
        return 'YOU SHALL PASS'
    else:
        return 'YOU SHALL NOT PASS'
    
#Задача №3
def amulet_area(a, b, c):
  import math
  p = (a+b+c)/2
  S = math.sqrt(p*(p-a)*(p-b)*(p-c))
  return Sэ

#Задача №4
def cal_euclidean(a, b):
  import numpy as np
  distance = np.sqrt(np.dot(a-b, a-b))
  return distance 

def cal_manhattan(a, b):
  import numpy as np
  distance = np.sum(np.abs(a-b))
  return distance

def cal_cosine(a, b):
    from numpy import dot
    from numpy.linalg import norm
    distance = dot(a, b)/(norm(a)*norm(b))
    return distance

#Задача №5
my_array = np.random.rand(100)
max_value = np.max(my_array)
min_value = np.min(my_array)
my_array = (my_array - min_value) / (max_value - min_value)
print(np.max(my_array), np.min(my_array))
print(my_array)

my_matrix = np.random.randint(0, 50, size = (5,6))
max_index = np.unravel_index(np.argmax(my_matrix), my_matrix.shape)
selected_column = my_matrix[:,max_index[1]]
print('Shape: ',my_matrix.shape)
print('Array')
print(my_matrix)
print(selected_column)

def get_unique_rows(X):
    X_unique = np.unique(X, axis =0)
    return X_unique
X = np.random.randint(4, 6, size=(10,3))
print(X)
get_unique_rows(X)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




