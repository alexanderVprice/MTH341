# %% [markdown]
# # <div align="center"> MTH341 In-Class 2
# #### <div align="center"> Defining functions in Python, Matricies
# <div align="right"> Alexander Price

# %% [markdown]
# #### <div align="center"> Python Functions

# %% [markdown]
# #### Exercise 1
# Read and predict the output of the following code:

# %%
def g(a,b):
    z=a+b
    return z
c=5
d=6
e=g(c,d)
print('c is',c)
print('d is',d)
print('e is',e)

# %% [markdown]
# After predicting the output, run the code and check the result.

# %% [markdown]
# #### Exercise 2
# Write a Python function that takes in two arguments, and returns 5 times the first argument minus 2 times the second argument. Then write code that calls your function with some chosen numbers, assigns the output to a variable and prints the result.

# %%
import numpy as np
def f(x,y):
    return 5*x-2*y

a = f(1,1)
print(a)
b = f(1/5,1/2)
print(b)

# %% [markdown]
# #### Exercise 3
# Write a Python function that takes in a value x, and returns the value sin(x)^5 + 2x +2.

# %%
import numpy as np
def f2(x):
    return np.sin(x)**5+2*x+2
print(f2(0))

# %% [markdown]
# #### Exercise 4
# Write a python function that takes two variables u and v, which should be nuympy vectors, and returns the projection of v onto u.
# Use your function to calculate proj_u(v) when u=(1,4,2) and v=(-2,6,3.1).

# %%
import numpy as np

def f3(u,v):
    return (u@v/u@u)*u

u = np.array([1,4,2])
v = np.array([-2,6,3.1])
print(f3(u,v))

# %% [markdown]
# #### <div align="center"> Matricies

# %% [markdown]
# #### Exercise 6
# Create a variable containing the matrix
# ```
# ( 6    2
#  -3.2  4
#    2  -2 )
# ```
# Using 2-d indexing, print out several elements of the array.
#
#

# %%
import numpy as np
m = np.array([[6,2],[-3.2  ,4],[2 , -2]])
print(m,"\n")
print(m[0],"\n")
print(m[:,0],"\n")
print(m[2,1],"\n")

# %% [markdown]
# #### Exercise 7
# Create a numpy arrary containing the matrix
# ```
# ( 2   -2    3
#   1    5    5
#   7    3   -1 )
# ```
# Using slice syntax, perform the row operation R1 <-- 3R1
#

# %%
import numpy as np

m = np.array([[2,-2,2],[1,5,5],[7,3,-1]])
m2 = np.array(m)
print(m,'\n')
m[0] = 3*m[0] #R1 <- 3R1
x=1
print(m)

# %% [markdown]
# #### Exercise 8
# Consider the linear system
# ```
# -2x - 3y + z  =  4
#  4x + 8y - 5z = -6
#  6x + 5y + 5z = -20
# ```
# Create the augmented matrix for this linear system as a 3x4 numpy array. Using slice syntax, perform all the row operations needed to transform the matrix into row-echelon form.

# %%
import numpy as np
m = np.array([[-2,-3,1,4],[4,8,-5,-6],[7,5,5,-20]])
m2 = np.array(m)
print(m,'\n')
m2[1]=m[1]+2*m[0]
m2[2]=m[2]-(7/4)*m[1]
print(m2,'\n')
m3 = np.array(m2)
m3[2]=m3[2]+(9/2)*m3[1]
print(m3)



