
from meshgrid import meshgrid
import math
import numpy as np
def makeOddOrientationCells(theta, lamba, sigma, gamma):
    sigma_x = sigma
    sigma_y = sigma / gamma

    nstds = 2
    xmax = np.max([abs(nstds * sigma_x * math.cos(math.pi / 2 - theta)),
                   abs(nstds * sigma_y * math.sin(math.pi / 2 - theta))])
    xmax = np.ceil(np.max([1, xmax]))
    ymax = np.max([abs(nstds * sigma_x * math.sin(math.pi / 2 - theta)),
                   abs(nstds * sigma_y * math.cos(math.pi / 2 - theta))])
    ymax = np.ceil(max([1, ymax]))
    xmin = -xmax
    ymin = -ymax

    [x, y] = meshgrid([p for p in range(int(xmin), int(xmax + 1))], [x for x in range(int(ymin), int(ymax + 1))])

    x_theta = x * math.cos(math.pi / 2 - theta) + y * math.sin(math.pi / 2 - theta)
    y_theta = -x * math.sin(math.pi / 2 - theta) + y * math.cos(math.pi / 2 - theta)

    msk = 1 / (2 * math.pi * sigma_x * sigma_y) * np.exp(
        -0.5 * (np.square(x_theta) / sigma_x ** 2 + np.square(y_theta) / sigma_y ** 2)) * np.cos(
        2 * math.pi / lamba * x_theta)
    msk = msk - np.mean(np.mean(msk))

    return msk

