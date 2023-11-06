import torch
import torch.nn as nn
from brain_region_GRUs import GRUs, GRUs_1band

class TransformerEncoders(nn.Module):
    def __init__(self):
        super(TransformerEncoders, self).__init__()
        N = [0, 5, 9, 6, 10, 6, 6, 9, 6, 5]
        self.N = N
        self.encoder_pf = nn.TransformerEncoderLayer(
            d_model=N[1]*5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_f = nn.TransformerEncoderLayer(
            d_model=N[2] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_lt = nn.TransformerEncoderLayer(
            d_model=N[3] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_c = nn.TransformerEncoderLayer(
            d_model=N[4] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_rt = nn.TransformerEncoderLayer(
            d_model=N[5] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_lp = nn.TransformerEncoderLayer(
            d_model=N[6] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_p = nn.TransformerEncoderLayer(
            d_model=N[7] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_rp = nn.TransformerEncoderLayer(
            d_model=N[8] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.encoder_o = nn.TransformerEncoderLayer(
            d_model=N[9] * 5,
            nhead=5,
            dim_feedforward=32,
            batch_first=True
        )
        self.local_GRUs = GRUs()

    def forward(self, x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o):
        batch, sequence, _, _ = x_pf.shape

        x_pf = torch.reshape(x_pf, (batch, sequence, self.N[1]*5))
        x_pf = self.encoder_pf(x_pf)
        x_f = torch.reshape(x_f, (batch, sequence, self.N[2] * 5))
        x_f = self.encoder_f(x_f)
        x_lt = torch.reshape(x_lt, (batch, sequence, self.N[3] * 5))
        x_lt = self.encoder_lt(x_lt)
        x_c = torch.reshape(x_c, (batch, sequence, self.N[4] * 5))
        x_c = self.encoder_c(x_c)
        x_rt = torch.reshape(x_rt, (batch, sequence, self.N[5] * 5))
        x_rt = self.encoder_rt(x_rt)
        x_lp = torch.reshape(x_lp, (batch, sequence, self.N[6] * 5))
        x_lp = self.encoder_lp(x_lp)
        x_p = torch.reshape(x_p, (batch, sequence, self.N[7] * 5))
        x_p = self.encoder_p(x_p)
        x_rp = torch.reshape(x_rp, (batch, sequence, self.N[8] * 5))
        x_rp = self.encoder_rp(x_rp)
        x_o = torch.reshape(x_o, (batch, sequence, self.N[9] * 5))
        x_o = self.encoder_o(x_o)

        x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o = self.local_GRUs(x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o)

        x_all = torch.stack([x_pf, x_f, x_lt, x_c, x_rt,
                              x_lp, x_p, x_rp, x_o], dim=2)

        return x_all