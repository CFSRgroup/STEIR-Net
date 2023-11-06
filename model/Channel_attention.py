import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange
N = [0, 5, 9, 6, 10, 6, 6, 9, 6, 5]


class Att_Layer(nn.Module):

    def __init__(self, input, output):
        super(Att_Layer, self).__init__()

        self.P_linear = nn.Linear(input, output, bias=True)
        self.V_linear = nn.Linear(input, 9, bias=False)

    def forward(self, att_input):
        # att_input = rearrange(att_input, 'b l f -> b (l f)')
        P = self.P_linear(att_input)

        feature = torch.tanh(P)
        alpha = self.V_linear(feature)
        # 下面开始softmax
        alpha = F.softmax(alpha, dim=2)
        out = torch.matmul(alpha, att_input)
        return out, alpha