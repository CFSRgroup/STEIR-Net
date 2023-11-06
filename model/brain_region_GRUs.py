import torch.nn as nn

# hidden size of GRUs
Dl = 32

class GRUs(nn.Module):
    def __init__(self):
        super(GRUs, self).__init__()
        N = [0, 5, 9, 6, 10, 6, 6, 9, 6, 5]
        self.GRU1 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[1]*5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU2 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[2] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU3 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[3] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU4 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[4] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU5 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[5] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU6 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[6] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU7 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[7] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU8 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[8] * 5,
            hidden_size=Dl,
            num_layers=1
        )
        self.GRU9 = nn.GRU(
            bidirectional=True,
            batch_first=True,
            input_size=N[9] * 5,
            hidden_size=Dl,
            num_layers=1
        )

    def forward(self, x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o):
        x_pf, _ = self.GRU1(x_pf)
        x_f, _ = self.GRU2(x_f)
        x_lt, _ = self.GRU3(x_lt)
        x_c, _ = self.GRU4(x_c)
        x_rt, _ = self.GRU5(x_rt)
        x_lp, _ = self.GRU6(x_lp)
        x_p, _ = self.GRU7(x_p)
        x_rp, _ = self.GRU8(x_rp)
        x_o, _ = self.GRU9(x_o)

        return x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o