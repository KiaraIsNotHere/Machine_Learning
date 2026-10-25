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
print(MATRIX.ndim)
print(MATRIX)