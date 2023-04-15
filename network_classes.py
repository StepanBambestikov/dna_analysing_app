import torch
import torch.nn as nn


class multi_nn_2layer_net(nn.Sequential):
    def __init__(self):
        super().__init__(
            nn.Linear(12, 8),
            nn.ReLU(inplace=True),
            nn.Linear(8, 3)
        )
        super().type(torch.FloatTensor)