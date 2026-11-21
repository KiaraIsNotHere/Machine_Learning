import torch as tch 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torch import nn


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


# Create A train/test split

train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]



# VISUALIZE VISUALIZE VISUALIZE

def plot_predic(train_data = X_train, train_label = y_train, 
                test_data = X_test, test_label = y_test, predictions = None):

    # Plots training data, test data and compares predictions
    plt.figure(figsize=(10, 7))

    # Plot training data in blue
    plt.scatter(train_data, train_label, c='b', s=4, label= "Training Data")

    # Plot test data in green
    plt.scatter(test_data, test_label, c='g', s=4, label= "Testing Data")
    
    # Are there prediscionts
    if predictions is not None:
        # Plot The predictions if they exist
        plt.scatter(test_data, predictions, c='r', s=4, label = 'Predictions')

    # Show The legend
    plt.legend(prop={"size": 14})
    plt.show()


# 2: Build A Model ------------------------------------------------------------------------------------------------------------------------------------------------------

# What our model does:
# - Start with random values (weight & Bias)
# - look at training data and adjust the random values to better represent (or get closer to) the ideal values (the weight & bias values we used to create the data)



class LineaerRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(tch.rand(1, 
                                            requires_grad = True,
                                            dtype= tch.float))

        self.bias = nn.Parameter(tch.randn(1,
                                           dtype= tch.float,
                                           requires_grad= True))

    # Fowrward method to define the computation in the model
    def forward(self, x: tch.Tensor) -> tch.Tensor:  # x is the input data
        return self.weight * x + self.bias # this is liear regression formula


### PyTorch Model Building Essentials
# torch.nn          - Contains all of the building for computational graps (A neural network can be considered a computational graph)
# torch.Parameter   - What parameters should our model try and learn, often a PyTorch layer from torch.nn will set these for us
# torch.nn.Module   - The base class for all neural netowrk modules, if you subclass it, you should overwrite forward()
# torch.optim       - this where the optimizers in PyTorch live, they will help with gradient descent
# def forward()     - All nn.Module subclasses require you to overwrite forward(), this method defines what happens in the forward computation


### Checking the contents of our PyTorch model
# Lets see whats inside
# Check model parameters using .parameters()

# Create a random seed
tch.manual_seed(42)

# Create an instance of the model (this is a subclass of nn.Module)
model_0 = LineaerRegressionModel()

# Check out the parameters
#print(list(model_0.parameters()))

# List named parameters
#print(model_0.state_dict())



### Making prediction using torch.inference_mode()
# to check our model predictive power, lets see how well it predics y_test based on X_test
# When we pass data through our model, its going to run it through the forward() method


# Make predictions with model
with tch.inference_mode():
    y_preds = model_0(X_test)



## 3. Train model
# The whole idea of training is for a model to move from some *unknown* parameters (these may be random) to some *known* parameters.

# or in other words from a poor representasion of the data to a better representation of the data

# one way to measure how poor or how wrong your models predictions are is to use a loss function

# Note: Loss function may also be called cost function or criterion in different areas. For our case, were going to refer to it as a loss functionn.

# - Loss function   : A function to measure how  wrong your model predictions are to the ideal output, lower is better
# - Optimizer       : Takes into account the loss of a model and adjust the models parameter (e.g weight & bias ) to improve loss function

# And specifically for PyTorch we need:
# A training lopp
# A test loop




