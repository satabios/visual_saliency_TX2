
from makeGauss import makeGauss
import numpy as np


def makeCentreSurround(std_center, std_surround):
    center_dim = int(np.ceil(3 * std_center))
    surround_dim = int(np.ceil(3 * std_surround))

    idx_center = np.asarray([dim for dim in range(-center_dim, center_dim + 1)])
    idx_surround = np.asarray([dim for dim in range(-surround_dim, 1 + surround_dim)])
    msk_center = np.asarray(makeGauss(idx_center, idx_center, std_center, std_center, 0))
    msk_surround = np.asarray(makeGauss(idx_surround, idx_surround, std_surround, std_surround, 0))

    msk = -msk_surround
    msk[(surround_dim - center_dim): (surround_dim + 1 + center_dim), (surround_dim  - center_dim): (
            surround_dim + 1 + center_dim)] =msk[(surround_dim - center_dim): ( \
            surround_dim + 1 + center_dim), (surround_dim  - center_dim): ( \
            surround_dim + 1 + center_dim)] + msk_center
    msk = msk - (np.sum(np.sum(msk))) / ((np.shape(msk)[0]) * (np.shape(msk)[1]))

    return msk
