import torch as tch 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1: Data (Prepare and load)
# 2: Build Model
# 3: Fitting the model to data (training)
# 4: Making predictions and evaluating a model (inference)
# 5: Saving and loading a model
# 6: Putting it all together





# 1: Data (Prepare and load) ------------------------------------------------------------------------------------------------------------------------------------------------------

# Create *Known* parameters
weight = 0.7
bias = 0.3

# Create
start = 0
end = 1
step = 0.02
X = tch.arange(start, end, step).unsqueeze(dim=1)
y = weight * X + bias


### Splitting data into training and test sets (one of the most important in machine learning in general)





