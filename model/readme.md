The **STEIR-Net.py** contains the backbone of the network.

The **transformer_encoders.py** contains the transformer encoders which resolve the features from different brain regions.

The **brain_region_GRUs.py** includes the GRUs which process the features obtained from the encoders.

The **Channel_attention.py** performs weight fusion of features from different brain regions.

The **mlp.py** is the multilayer perceptron.