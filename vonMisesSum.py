

from vonMisesPyramid import vonMisesPyramid
import numpy as np
def vonMisesSum(csPyr,vmPrs):



    maxLevel = vmPrs['maxLevel']
    vmPyr1, msk1,vmPyr2,msk2 = vonMisesPyramid(csPyr,vmPrs)

    map1 = vmPyr1['data']
    map2 = map1

    for ori in range(vmPrs['numOri']):
        for l in range(10):
            print(l)
            for k in range(l,10):

                if(l!=k):

                    map1[ori][l] = map1[ori][l] + (0.5**(l-1)) * (np.resize(vmPyr1['data'][ori][l][k],vmPyr1['data'][ori][l][k].shape))
                    map2[ori][l] = map1[ori][l] + (0.5 ** (l - 1)) * (np.resize(vmPyr2['data'][ori][l][k], vmPyr1['data'][ori][l][k].shape))
                else:
                    map1[ori][l] = np.zeros((map1[ori][l].shape))
                    map2[ori][l] = np.zeros((map2[ori][l].shape))

    return map1, msk1,map2,msk2