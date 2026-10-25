import numpy as np


# Shape --------------------------------------------------------------------------------------------------

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

# Indexing --------------------------------------------------------------------------------------------------
# ary[start:stop:step]

"""
arr = np.arange(24).reshape(2, 3, 4)
print("Original 3D array:\n", arr)

# Example 1: Slice first block (axis 0)
first_block = arr[0, :, :]
print("\nFirst block:\n", first_block)

# Example 2: Slice second row from all blocks
second_row_all_blocks = arr[:, 1, :]
print("\nSecond row from all blocks:\n", second_row_all_blocks)

# Example 3: Slice first two columns from all blocks and rows
first_two_cols = arr[:, :, 0:2]
print("\nFirst two columns from all blocks and rows:\n", first_two_cols)

# Example 4: Slice a sub-array (block 1, rows 0-1, columns 1-3)
sub_array = arr[1, 0:2, 1:4]
print("\nSub-array (block 1, rows 0-1, cols 1-3):\n", sub_array)

# Example 5: Using step in slicing (every other column)
every_other_col = arr[:, :, ::2]
print("\nEvery other column:\n", every_other_col)

# Example 6: Negative indexing (last block, last row)
last_block_last_row = arr[-1, -1, :]
print("\nLast block, last row:\n", last_block_last_row)
"""



#print(f"The second array, first nested array, 4th position: {tiga_dimensi[1,0,3]}")

# Check how many dimension the arrays have
"""print(tiga_dimensi.ndim)
print(tiga_dimensi.shape)"""

# Create an array with n (5) dimensions
#arr = np.array([1,2,3,4,5], ndmin= 5)

# ReShape --------------------------------------------------------------------------------------------------
# it returned like view (look below)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

duaDim = arr.reshape(2, 6) # 1D -> 2D
tigaDim = arr.reshape(2, 3, 2) # 1D -> 3D
jadisatu = arr.reshape(2, 3, 2) # 3D -> 1D

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


# Copy vs view


arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() # the arr will not change
y = arr.view() # the arr will change

y[0] = 31 # the arr will change
#print(x)

# Join --------------------------------------------------------------------------------------------------

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

add = tiga_dimensi.ndim
print(add)