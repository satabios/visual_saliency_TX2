
import time
import numpy as np
from calcSigma import  calcSigma
from makeCentreSurround import  makeCentreSurround

def makeDefaultParams(w):
    minLevel = 1
    maxLevel = 10

    downSample = 'half'

    params = {}

    params['channels'] = 'ICO'
    params['maxLevel'] = maxLevel

    ori = np.asarray( [0, 45])
    oris = np.zeros((4))
    oris[:2] = np.deg2rad(ori)
    oris[2:4] = np.deg2rad(ori + 90)


    [sigma1, sigma2] = calcSigma(2, 3)

    params['csPrs'] = {}

    params['csPrs']['inner'] = sigma1
    params['csPrs']['outer'] = sigma2
    params['csPrs']['depth '] = maxLevel
    params['csPrs']['downSample'] = downSample

    start = time.time()
    msk = makeCentreSurround(params['csPrs']['inner'], params['csPrs']['outer'])
    temp = msk[round(msk.shape[0] / 2.0)-1, :]

    temp[temp > 0] = 1
    temp[temp < 0] = -1
    zc = temp[round(msk.shape[1]/ 2.0)-1:-1] - temp[round(msk.shape[0]/ 2.0):]
    R0 = 2#np.where(abs(zc) == 2)[0][0]
    print('\nCenter Surround Radius is %d pixels. \n', R0)

    print(time.time() - start, '\n')
    params['gaborPrs'] ={}
    params['gaborPrs']['lamba'] = 8
    params['gaborPrs']['sigma'] = 0.4 * params['gaborPrs']['lamba']
    params['gaborPrs']['gamma'] = 0.8
    params['evenCellPrs'] ={}
    params['evenCellPrs']['minLevel'] = minLevel
    params['evenCellPrs']['maxLevel'] = maxLevel
    params['evenCellPrs']['oris'] = oris
    params['evenCellPrs']['numOri'] = len(oris)
    params['evenCellPrs']['lamba'] = 4
    params['evenCellPrs']['sigma'] = 0.56 * params['evenCellPrs']['lamba']
    params['evenCellPrs']['gamma'] = 0.5
    params['oddCellPrs'] ={}
    params['oddCellPrs']['minLevel'] = minLevel
    params['oddCellPrs']['maxLevel'] = maxLevel
    params['oddCellPrs']['oris'] = oris
    params['oddCellPrs']['numOri'] = len(oris)
    params['oddCellPrs']['lamba'] = 4
    params['oddCellPrs']['sigma'] = 0.56 * params['evenCellPrs']['lamba']
    params['oddCellPrs']['gamma'] = 0.5
    params['bPrs'] = {}
    params['bPrs']['inLevel'] = minLevel
    params['bPrs']['axLevel'] = maxLevel
    params['bPrs']['numOri'] = len(oris)
    params['bPrs']['alpha'] = 1
    params['bPrs']['oris'] = oris
    params['bPrs']['CSw'] = 1
    params['vmPrs'] ={}
    params['vmPrs']['minLevel'] = minLevel
    params['vmPrs']['maxLevel'] = maxLevel
    params['vmPrs']['oris'] = oris
    params['vmPrs']['numOri'] = len(oris)
    params['vmPrs']['R0'] = R0
    params['giPrs'] ={}
    params['giPrs']['w_sameChannel'] = 1
    params['tPrs'] = {}
    params['tPrs']['w'] = w

    return params
