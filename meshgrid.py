import numpy.matlib as mat
import numpy as np
def meshgrid(x,y):
    x = np.asarray(x)
    y = np.asarray(y)
    xrow = x.reshape(1,len(x))  # % Make sure x is a full row vector.
    ycol = y.reshape(len(y),1)  # % Make  sure y is a full column     vector. \
    xx = mat.repmat(xrow, len(ycol),1)
    yy = mat.repmat(ycol,1, xrow.shape[1])  # 7*7

    return xx, yy
