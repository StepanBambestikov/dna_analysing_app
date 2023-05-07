import torch
import torch.nn as nn

begin_nn_column = 0
end_nn_column = 11
begin_Na_column = 12
end_Na_column = 18
Activity_column = 7 # activity number
Na_factor = 0.006


class multi_nn_2layer_net(nn.Sequential):
    def __init__(self):
        super().__init__(
            nn.Linear(12, 8),
            nn.ReLU(inplace=True),
            nn.Linear(8, 3)
        )
        super().type(torch.float64)


class Ne_conv_net(nn.Module):
    def __init__(self, input_vector_size=4):
        super().__init__()
        self.fc = nn.Linear(input_vector_size, 2).type(torch.float64)

    def forward(self, nearest_neibours, Na_data):
        result = self.fc(torch.cat((nearest_neibours, Na_data), dim=1))
        return result


class conv2d_net_06_05(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=20, kernel_size=(4, 4), padding=(0, 1))
        self.max_pool = nn.MaxPool2d(kernel_size=(1, 2))
        self.conv_relu = nn.ReLU(inplace=True)
        self.flatten = nn.Flatten(start_dim=1, end_dim=-1)
        linear_input = 300
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(linear_input, 3)
        )
        self.Na_net = Ne_conv_net(input_vector_size=linear_input + 8)

    def forward(self, input):
        dna_data, Na_data = input
        conv_out = self.conv(dna_data[:, None, :])
        dna_data = self.max_pool(conv_out)
        dna_data = self.flatten(dna_data)
        Na_out = self.Na_net(dna_data.type(torch.float64), Na_data)

        dna_data = self.conv_relu(dna_data)
        result = self.linear_relu_stack(dna_data)

        dS_activity_additive = Na_out[:, 0] * torch.log(Na_data[:, Activity_column]) * Na_factor
        dG_activity_additive = Na_out[:, 1] * torch.log(Na_data[:, Activity_column]) * Na_factor
        # summary
        result[:, 2] += dS_activity_additive
        result[:, 1] += dG_activity_additive
        return result


class linear_net_06_05(nn.Module):
    def __init__(self):
        super().__init__()
        self.origin_net = multi_nn_2layer_net()
        self.Ne_net = Ne_conv_net(12 + 8)

    def forward(self, input):
        nearest_neibours, Na_data = input
        #Na args preparation
        Na_coeffitient = self.Ne_net(nearest_neibours, Na_data) # todo исправить потом
        dS_activity_additive = Na_coeffitient[:, 0] * torch.log(Na_data[:, Activity_column]) * Na_factor
        dG_activity_additive = Na_coeffitient[:, 1] * torch.log(Na_data[:, Activity_column]) * Na_factor
        #Main nn preparation
        result = self.origin_net(nearest_neibours)
        result[:, 2] += dS_activity_additive
        result[:, 1] += dG_activity_additive
        return result
