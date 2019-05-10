import numpy as np
import sklearn




class myNeural:
    def __init__(self, X, Y, layer_size):
        in_size, out_size, l_size = self.set_layer_size(X, Y, layer_size)
    
    def set_layer_size(self, X, Y, layer_size):
        hx = X.shape[0]
        hy = Y.shape[0]
        ls = layer_size

        return hx, hy, ls

    def init_param(self):
        np.rand.rd

    def forward_prop():


    def compute_cost():

    def backward_prop():

    def update_param():

    def NNmodel():

    def predict():


    