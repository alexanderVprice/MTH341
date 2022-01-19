# %% [markdown]
# # <div align="center"> MTH341 In-Class 3
# #### <div align="center"> Python Linear-System Solver, Polynomial interpolation
# <div align="right"> Alexander Price

# %% [markdown]
# #### <div align="center"> Linear-System Solver

# %% [markdown]
# #### Exercise 1
# Find the solutions to the following linear system:
# ```
# 7x - 2y + 5z =   3
#       y +  z = -12
#  x - 2y - 3z =   2
#  ```
#

# %%
import numpy as np

s = np.array([[7,-2,5],[0,1,1],[1,-2,-3]])
v = np.array([3,-12,2])
xyz = np.linalg.solve(s,v)
print("x = ",round(xyz[0],2))
print("y = ",round(xyz[1],2))
print("z = ",round(xyz[2],2))

# %% [markdown]
# #### <div align="center"> Polynomial Interplation

# %% [markdown]
# #### Exercise 2
# Find the quadratic polynomial that pases through the points
# ```
# (1.4, 6),
# (2.1, 3),
# (3.9, 4)
# ```

# %%
import numpy as np
x0 = np.array([1,1,1])
x1 = np.array([1.4,2.1,3.9])
x2 = np.array(x1**2)
s = np.array([[x2[0],x1[0],x0[0]],[x2[1],x1[1],x0[1]],[x2[2],x1[2],x0[2]]])
y = np.array([6,3,4])
abc = np.linalg.solve(s,y)
print("a = ",round(abc[0],2))
print("b = ",round(abc[1],2))
print("c = ",round(abc[2],2))





# %% [markdown]
# #### Exercise 3
# Write a python function that takes as its argument 3 ordered pairs (they may be either tuples or vecgtors), and returns a vector containing the coefficients of the quadratic polynomial that passes through these three 3 points

# %%
import matplotlib.pyplot as plt
import numpy as np
def quadraticCoefficients(p1,p2,p3):
    x0 = np.array([1,1,1])
    x1 = np.array([p1[0],p2[0],p3[0]])
    x2 = np.array(x1**2)
    s = np.array([[x2[0],x1[0],x0[0]],[x2[1],x1[1],x0[1]],[x2[2],x1[2],x0[2]]])
    y = np.array([p1[1],p2[1],p3[1]])
    abc = np.linalg.solve(s,y)
    return abc

abc = quadraticCoefficients((1.4,6),(2.1,3),(3.9,4))
print("a = ",round(abc[0],2))
print("b = ",round(abc[1],2))
print("c = ",round(abc[2],2))

# %% [markdown]
# #### Exercise 4
# Extend this concept to the cubic polynomial passing through 4 points and determine the cubic polynomial that goes through the points
# ```
# ( 1, 3.4 ),
# ( 2, 1.8 ),
# ( 3, 2.1 ),
# ( 4, 6.7 )
# ```
# Using either matplotlib in python (or in desmos), graph the cubic polynomial and all 4 of these points.

# %%
import matplotlib.pyplot as plt
import numpy as np

x0 = np.array([1,1,1,1])
x1 = np.array([1,2,3,4])
x2 = np.array(x1**2)
x3 = np.array(x1**3)
s = np.array(  [  [x3[0],x2[0],x1[0],x0[0] ] , [ x3[1],x2[1],x1[1],x0[1] ] , [ x3[2],x2[2],x1[2],x0[2] ] , [ x3[3],x2[3],x1[3],x0[3] ]  ]  )
y = np.array([3.4,1.8,2.1,6.7])
abcd = np.linalg.solve(s,y)
a = abcd[0]
b = abcd[1]
c = abcd[2]
d = abcd[3]
x = np.linspace(0,5,1E3)
y = a*x**3 + b*x**2 + c*x + d
plt.plot(x,y)
plt.plot( 1, 3.4, marker='o')
plt.plot( 2, 1.8, marker='o')
plt.plot( 3, 2.1, marker='o')
plt.plot( 4, 6.7, marker='o')