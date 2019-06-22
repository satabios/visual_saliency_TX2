

import numpy as np
from sumPyr import sumPyr
from maxNormalizeLocalMax import  maxNormalizeLocalMax

def normCSPyr2(csPyr1,csPyr2,m):

    temp = sumPyr(csPyr1, csPyr2, 0)
    for l in range(len(csPyr1)):

        norm = maxNormalizeLocalMax(temp[l],[0,10])
        if(np.max(np.max(temp[l]))):
            scale = np.max(np.max(norm))/np.max(np.max(temp[l]))
        else:
            scale = 0

        csPyr1[l] = scale * csPyr1[l]
        csPyr2[l] = scale * csPyr2[l]



    return csPyr1,csPyr2