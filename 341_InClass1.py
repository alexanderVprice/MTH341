# %% [markdown]
# # <div align="center"> MTH341 In-Class 1
# #### <div align="center"> Vectors and Matricies in Python/Numpy
# <div align="right"> Alexander Price

# %% [markdown]
# ## Exercise 1
# Let v1 = (2,3,5), v2 = (7,1,-3), v3 = (0,2,1)
#
# i) Enter these as numpy vectors and compute y = 3v1 + 6v2-5v3. Display it
#
# ii) Create a new vector w that is a linear combination of v1 and v3. Display it
#
# iii) Compute the dot product v1 * v2. Display it.
#
# iv) Compute the norm ||v1|| = sqrt(v1*v2). Display it.
#
# v) Compute the angle between the vector v1 and the vector v2. Convert this to degrees.
#

# %%
import numpy as np
#i)
v1 = np.array([2,3,5])
v2 = np.array([7,1,-3])
v3 = np.array([0,2,1])
y = 3*v1+6*v2-4*v3
print("  i) ",y)
#ii)
w = 2*v1+v2
print(" ii) ",w)
#iii)
v1dotv2 = v1@v2
print("iii) ",v1dotv2)
#iv)
magV1 = np.linalg.norm(v1)
print(" iv) ",magV1)
#v)
np.angle
magV2 = np.linalg.norm(v2)
angle = np.rad2deg(np.arccos(v1@v2/(magV1*magV2)))
print("  v) ",angle)

# %% [markdown]
# ## Exercise 2
# Let A,B,C be the points *1,2), (3,5), (-1,4) in the plane
#
# i) Create 3 Python arrays named A,B,C that are vectors for these points\
#
# ii) Compute the displacement vectors AB, AC (using Python), and assign these as Python arrays. Use this to calculate the angle BAC of the triangle. Convert to degrees.
#
# iii) Using the same process, find the angle ABC and the angle BCA. Check that the sum of these equals 180.

# %%
import numpy as np
#i)
A = np.array([1,2])
B = np.array([3,5])
C = np.array([-1,4])
print("  i) A, B, C : ",A,B,C,"\n")
#ii)
AB=B-A
AC=C-A
magAB = np.linalg.norm(AB)
magAC = np.linalg.norm(AC)
angleBAC=np.rad2deg(np.arccos(AB@AC/(magAB*magAC)))
print(" ii) BAC = ",angleBAC)
#iii)
BA=A-B
BC=C-B
magBA = np.linalg.norm(BA)
magBC = np.linalg.norm(BC)
angleABC=np.rad2deg(np.arccos(BA@BC/(magBA*magBC)))

CA=A-C
CB=B-C
magCA = np.linalg.norm(CA)
magCB = np.linalg.norm(CB)
angleBCA=np.rad2deg(np.arccos(CA@CB/(magCA*magCB)))
print("     AB, AC, BA, BC, CA, CB :\n    ",AB,AC,BA,BC,CA,CB,"\n")
sum = angleABC + angleBAC + angleBCA
print("iii) BAC, ABC, BCA, sum :\n    ",round(angleBAC,2),round(angleABC,2),round(angleBCA,2),sum)



