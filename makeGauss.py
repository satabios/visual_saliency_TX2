import  numpy as np
import math
from meshgrid import  meshgrid

def makeGauss(dim1, dim2, sigma_1, sigma_2, theta):
    x0 = 0
    y0 = 0

    norm = 1

    msk = np.zeros((dim1.shape[0],1))
    [X, Y] = meshgrid(dim1, dim2)  # stopped here  ; )

    a = math.cos(theta) ** 2 / 2 / sigma_1 ** 2 + math.sin(theta) ** 2 / 2 / sigma_2 ** 2
    b = -math.sin(2 * theta) / 4 / sigma_1 ** 2 + math.sin(2 * theta) / 4 / sigma_2 ** 2
    c = math.sin(theta) ** 2 / 2 / sigma_1 ** 2 + math.cos(theta) ** 2 / 2 / sigma_2 ** 2

    if norm:

        msk = 1 / (2 * math.pi * sigma_1 * sigma_2) * np.exp(- (a * (X - x0) ** 2 + 2 * b * (X - x0) * (Y - y0) + c * (Y - y0) ** 2))
    else:
        msk = math.exp(- (a * (X - x0) ** 2 + 2 * b * (X - x0) * (Y - y0) + c * (Y - y0) ** 2))

    return msk