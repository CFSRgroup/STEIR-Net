import torch
import torch.nn as nn
from transformer_encoders import TransformerEncoders
from mlp import mlp
from Channel_attention import Att_Layer
from einops import rearrange


class backBone(nn.Module):
    def __init__(self):
        super(backBone, self).__init__()
        self.transformer_encoder_layer = TransformerEncoders()

        self.Brain_region_Att_layer = Att_Layer(input=64, output=64)

        self.biLSTM = nn.LSTM(
            bidirectional=True,
            batch_first=True,
            input_size=576,
            hidden_size=155,
            num_layers=1,
            # dropout=0.5
        )
        # self.SE = SE_Block(ch_in=8)

        self.MLP = mlp()

    def forward(self, x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o):
        x_all = self.transformer_encoder_layer(x_pf, x_f, x_lt, x_c, x_rt, x_lp, x_p, x_rp, x_o)
        batch, sequence, lobe, f = x_all.shape
        x_all_out = []
        all_br_weight = []
        for i in range(0, sequence):
            x, br_weight = self.Brain_region_Att_layer(x_all[:, i, :, :].squeeze())
            x_all_out.append(x)
            all_br_weight.append(br_weight)
        x_all = torch.stack(x_all_out,dim=1)
        all_br_weight = torch.stack(all_br_weight, dim=1)
        x_all = rearrange(x_all, 'b s l f -> b s (l f)')
        x_all, _ = self.biLSTM(x_all)
        # x_all = x_all[:,:,:310]
        # x_all = self.SE(x_all)

        batch, sequence, f = x_all.shape
        output = []
        for i in range(0,sequence):
            x = self.MLP(x_all[:,i,:].squeeze())
            output.append(x)

        output = torch.hstack(output)

        return output, all_br_weight