import numpy as np



# 0 Dimension array
nol_dimensi = np.array(67)

# 1 Dimension array
satu_dimensi = np.array([1,2,3,4,5])    

# 2 Dimension array
dua_dimensi = np.array([
                        [1,2,3,4,5],
                        [6,7,8,9,10]
                        ])
# Acces the element on first row,second column
#print(f"The 2nd element on 1st row: {dua_dimensi[0,1]}")



# 3 Dimension array
tiga_dimensi = np.array([
                        [[1,2,3,4,5],                   [6,7,8,9,10]],
                        [['a','b','c','d','e'],         ['f','g','h','i','j']],
                        [["1A",'2B','3C','4D','5E'],    ["6F",'7G','8H','9I','10J']]
                        ])

# [first array, second nested array, position] 
#print(f"The second array, first nested array, 4th position: {tiga_dimensi[1,0,3]}")

# Check how many dimension the arrays have
#print(tiga_dimensi.ndim)

# Create an array with n (5) dimensions
#arr = np.array([1,2,3,4,5], ndmin= 5)



# Data Types --------------------------------------------------------------------------------------------------
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""
#arr = np.array([1, 2, 3, 4], dtype='i4') # Create an array with data type 4 bytes intege
#arr = np.array([1, 2, 3, 4], dtype='S') # Creating Arrays With a Defined Data Type

#print(arr.dtype)

#arr = np.array([1.1, 2.1, 3.1]) 
#newarr = arr.astype('i') Converting Data Type on Existing Arrays