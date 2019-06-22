

import numpy as np
from vonMisesSum import vonMisesSum

def borderPyramid(csPyrL,csPyrD,cPyr,params):


    data = (csPyrL,csPyrL,csPyrL,csPyrL)
    ori = np.zeros((4,10))
    invmsk_set  = np.zeros((4,10,13,13))
    bPyr1 = {'data':data,'ori':ori,'invmsk':invmsk_set}
    bPyr3 = bPyr1

    bPrs = params['bPrs']
    vmPrs = params['vmPrs']

    vmL1, msk1, vmL2, msk2 = vonMisesSum(csPyrL, vmPrs)
    vmD1, csmsk1, vmD2, csmsk2 = vonMisesSum(csPyrD, vmPrs)

    for ori in range(bPrs['numOri']):

        for l in range(10):
            bPyr1['ori'][ori][l] = msk1['ori'][ori][l]
            bPyr1['invmsk'][ori][l][:] = msk1['data'][ori]

            bPyr3['ori'][ori][l] = msk1['ori'][ori][l]
            bPyr3['invmsk'][ori][l][:] = msk1['data'][ori][l]


            # cPyr(l).orientation(ori).data. * (1 + bPrs.alpha. * (vmL1(l).orientation(ori).data - bPrs.CSw. * vmD2(l).orientation(ori).data))
            bPyr1['data'][ori][l] = cPyr[l][ori] * (1+ bPrs['alpha'] *(vmL1[ori][l] - bPrs['CSw'] * vmD2[ori][l]))
            bPyr1['data'][ori][l][(bPyr1['data'][ori][l]<0).astype(int)] = 0

            bPyr3['data'][ori][l] = cPyr[l][ori] * (1+ bPrs['alpha'] *(vmD1[ori][l] - bPrs['CSw'] * vmL2[ori][l]))
            bPyr3['data'][ori][l][(bPyr3['data'][ori][l] < 0).astype(int)] = 0






    return bPyr1,bPyr3