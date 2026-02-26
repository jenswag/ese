# Enhanced Stokes-Einstein (ESE): functions/models.py
# Models
# ---
# Jens Wagner, 05.11.2025
# ----------------------------------------------------------------------------------------------------------------------

# Import Packages and Modules
import numpy as np

import torch.nn as nn
import torch.nn.functional as F


# Neural Network (NN)
class NN(nn.Module):
    def __init__(self, input_size=12, hidden_size=32, output_size=1, layers=2, activation_function=nn.ReLU()):
        super(NN, self).__init__()
        self.activation_function = activation_function
        self.layers = nn.ModuleList()

        # Input layer
        self.layers.append(nn.Linear(input_size, hidden_size))

        # Hidden
        prev_size = hidden_size
        for _ in range(1, layers):
            next_size = max(prev_size // 2, output_size)
            self.layers.append(nn.Linear(prev_size, next_size))
            prev_size = next_size

        # Output layer
        self.layers.append(nn.Linear(prev_size, output_size))

    def forward(self, x):
        for layer in self.layers[:-1]:
            x = self.activation_function(layer(x))
        x = self.layers[-1](x)
        return F.softplus(x)


# Define Stokes-Einstein (SE) and Stokes-Einstein Gierer-Wirtz Estimation (SEGWE)
# SE: M -> D
def SE(mma_i, eta_j, tmp_j, packing=0.64, rho_bulk=1.05e3, k_B=1.380649e-23, N_A=6.02214076e23):

    sdc = (k_B * tmp_j) / (6 * np.pi * eta_j * np.cbrt((3 * packing * mma_i) / (4 * np.pi * rho_bulk * N_A)))

    return sdc
