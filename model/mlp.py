import torch.nn as nn

class mlp(nn.Module):
    def __init__(self):
        super(mlp, self).__init__()

        # self.fc1 = nn.Sequential(
        #     nn.Linear(in_features=310, out_features=32),
        #     # nn.Tanh()
        # )
        self.fc2 = nn.Sequential(
            nn.Linear(in_features=310, out_features=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        # x = self.fc1(x)
        output = self.fc2(x)

        return output