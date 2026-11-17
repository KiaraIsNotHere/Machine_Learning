import torch as tch 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### Tensor ----------------------------------------------------------------------------------------------------------------

# Rank 0 tensor --> Scalar
# Rank 1 tensor --> Vector
# Rank 2 tensor --> Matrix
# Rank 3 tensor --> Higher dimensional array (e.g.,cubes, hypercubes)


# Scalar
scalar = tch.tensor(7)

# Vector
vector = tch.tensor( [7, 7, 7] )



# MATRIX 
MATRIX = tch.tensor([[1,2], [11,12]])
#print(MATRIX.ndim)
#print(MATRIX)



# TENSOR
TENSOR = tch.tensor([[[1,2,3],
                      [4,5,6],
                      [7,8,9]]])
#print(TENSOR.shape) --> torch.size([1,3,3])

# img for make it more understand
img = "image/ndim of tensor.png" # --> dari tensor diatas 1 = kurung ungu, 3 = kurung biru, 3 = kurung ungu

### Random tensor
# Start with random numbers -> look at data  -> update random numbers - > look at data -> update random numbers


# Create a random tensor of size (3, 4)
random_tensor = tch.rand(3, 4)


# Create a random tensor with similar shape to an image tensor
rand_img_size_tensor = tch.rand(size=(224, 224, 3)) # height, width, colour channel

# tensor of zeros and ones
nol = tch.zeros(1,5) # satu = tch.ones(5,6)

### Creating a range of tensors and tensors like
arange = tch.arange(0, 10)

ten_zeros = tch.zeros_like(arange)


### Tensor datatypes
# Tensor datatypes is one of the big 3 errors youll run into with PyTorch & deep learning:
# 1. Tensors not in right datatypes
# 2. Tensors not in right shape
# 3. Tensors not on the right device

float_32 = tch.tensor([3.0,4.2,6,7],
                      dtype= None, # What datatype is the tensor ( float 32 or float16 )
                      device= "cpu", # What device is your tensor on 
                      requires_grad= False) # Whether or nor to track gradients with this tensor operations


float_16 = float_32.type(tch.float16)


int_32 = tch.tensor([1,5,8], dtype=tch.long)


### Getting information from tensors (tensor attributes)

# 1. Tensors not in right datatypes - to do get datatype from a tensor, can use tensor.dtype
# 2. Tensors not in right shape - to get shape from a tensor, can use tensor.shape
# 3. Tensors not on the right device - to get device from a tensor, can use tensor.device



# Create a tensor
some_tensor = tch.rand(3,4)


# Find out details about some tensor
"""print(some_tensor)
print(f"Datatype of tensor: {some_tensor.dtype}")
print(f"Shape of tensor: {some_tensor.shape}")"""

### Manipulating Tensors (tensor operations)

# Tensor operations include:
# * Addition
# * Substraction
# * Multiplication (element - wise)
# * Division
# * Matrix multiplication

# Create a tensor
tensor = tch.tensor([1,2,3])

"""
tensor += 10 # Addition
tensor -= 10 # Substraction
tensor *= 10 # Multiplication
tensor /= 10 # Division
"""

# PyTorch built in functions
tch.mul(tensor, 10) # Multiplication
tch.add(tensor, 10) # Addition

### Matrix Multipication ( 2 main ways of performing multiplicationin neural networks and deep learning)

# 1.Element - Wise Multiplication
# 2.Matrix Multiplication


# Element Wise Multiplication
#print(tensor, "*", tensor)
#print(f"Equals: {tensor * tensor}")

# Matrix Multiplication ( @ )
tch.matmul(tensor, tensor)


#### Two main rules that performing matrix mutlipication needs to satisfy:
# 1. The inner Dimension must match : (3, 2) @ (3, 2) wont work, (3, 2) @ (2, 3) will work

# 2. The resulting matrix has the shape of the outer dimensions


### One of the most common error : Shape errors
tensor_A = tch.tensor([[1, 2],
                       [3, 4],
                       [5, 6]])

tensor_B = tch.tensor([[7, 10],
                       [8, 11],
                       [9, 12]])

# tch.mm(tensor_A, tensor_B) # tch.mm is the same as tch.matmul 

# tch.matmul(tensor_A, tensor_B) # Wont work because (3, 2) @ (3, 2)

# To fix our shape issues, we can manipulate the shape of one our tensorts using a transpose (A transpose swtiches the axes or dimensions of a given tensor)
# print(tensor_B.T)


# The matrix multiplication operation works when tensor_B is transposed

"""
print(f"Original Shapes: Tensor_A = {tensor_A.shape} | Tensor_B = {tensor_B.shape}")
print(f"New shapes: Tensor_A = {tensor_A.shape} (same shape as above) | tensor_B.T = {tensor_B.T.shape}")

print(f"Multiplying: {tensor_A.shape} @ {tensor_B.T.shape} <-- Inner dimensions must match")
print("Output:\n ")
output = tch.matmul(tensor_A, tensor_B.T)
print(output)
print(f"\nOutput shape: {output.shape}")
"""

### Finding the min, max, mean, sum, etc (tensor aggregation)

x = tch.arange(0, 100 + 1, 10)

# max or min - change the min or max
tch.min(x), x.min

# Find the mean - need to be a float
#print(tch.mean(x.type(tch.float64))), x.type(tch.float32).mean()


### Finding the positional min and max

# Find the position in tensor that has the minimum value with argmin() -> return index position of target tensor where the minimum valude occurs
x.argmin() 



# Find the position in tensor that has the minimum value with argmin()
x.argmax()


### Reshaping, Stacking, Squeezing and unsqueezing tensors

# Reshaping - reshapes an input to a defined shape
# View - return a view of an input tensor of certain shape but keep the same memory as the original tensor
# Stacking - combine multiple tensors on top of each other (vstack) or side by side
# Squeeze - removes all '1' dimensions from a tensor
# Unsqeeze - add a '1' dimension to a target tensor
# Permute - return a view of the input with dimensions permuted (swapped) in a certain way


# Create a tensor

x = tch.arange(1., 10.)

# Add an extra dimension
x_reshaped = x.reshape(1, 9)


# Change the view 
z = x.view(1, 9)

# Changing z changes x (because a view of a tensor shares the same memory as the original input)
z[:, 0] = 5

# Stack tensors on top of each other
x_stacked = tch.stack([x, x, x, x], dim=0)
#print(x_stacked)


## torch.squezee - removes all single dimensions from a target tensor
#print("Previous Tensor - Shape",x_reshaped, x_reshaped.shape)


# Remove extra dimensions from x_reshaped
x_squeezed = x_reshaped.squeeze()
#print(f"\nNew tensor: {x_squeezed} and size {x_squeezed.shape}")



# torch.unsqueeze() - adds a single dimension to a target tensor at a specific dim (dimension) |     Menghilangkan dimensi
#print(f"Previous target: {x_squeezed}")
#print(f"Previous shape: {x_squeezed.shape}")

# Add an extra dimension with unsqueeze   | Menambah dimensi
x_unsqueezed = x_squeezed.unsqueeze(dim=0)
#print(f"\nNew tensor: {x_unsqueezed} | Shape: {x_unsqueezed.shape}")



# torch.permute - rearranges the dimensions of a target tensor in a specified order
x_original = tch.rand(size=(224, 224, 3)) # [weight, width, colour_channel]


# permute the original tensor to rearrange the axis (or dim) order |        Merubah urutan
x_permuted = x_original.permute(2, 0, 1) # Shift axis 224 -> Kedua, 224 -> ketiga, 3 -> pertama


### Indexing (selecting)

x = tch.arange(1, 10).reshape(1, 3 ,3)


# Index on our tensor
#print(f"Angka 9: {x[0, 2, 2]}")


# You can also use ":" to select "all of the target dimension"
#print(x[:, 0])


# Get all values of 0th and 1st dimensions but only index 1 of 2nd dimension
#print(x[:, :, 1])

# Get all values of the 0 dimension but only the 1 index value of 1st and 2nd dimension
#print(x[:, 1, 1])

# Get index 0 of 0th and 1st dimension and all values of 2nd dimension
#print(x[0, 0, :])




### NumPy

# NumPy array to tensor

array = np.arange(1.0, 8.0)
tensor = tch.from_numpy(array) # Will be torch.float64

# Change the value of arraay
array += 1

# Tensor to NumPy array
tensor = tch.ones(7)
numpy_tensor = tensor.numpy()

# Foot Notes: both dont share same memory



### Reproducbility (trying to take random out of random)
# in short
# Start with random numbers -> tensor operations -> update random numbers to try and make them better representasions of the data -> again -> again -> again -> again ....


# To reduce the randomness in neural networks and PyTorch comes in the concept of a 'random seed'
# Essentialy what the random seed does in "flavour" the randomness

rand_tens_A = tch.rand(3, 4)
rand_tens_B = tch.rand(3, 4)


# Make some random but reproducible tensors

# Set the random seed
tch.manual_seed(67) # Only work with 1 block of code

rand_tens_C = tch.rand(3, 4)

tch.manual_seed(67)
rand_tens_D = tch.rand(3, 4)

#print(rand_tens_C)
#print(rand_tens_D)
#print(rand_tens_C == rand_tens_D)



### Running tensors and PyTorch objects on the gpu (and making faster computations)

# Check for GPU acces with PyTorch
#print(tch.cuda.is_available())

# Setup device agnostic code
device = 'cuda' if tch.cuda.is_available() else 'cpu'