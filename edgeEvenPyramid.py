#
# from validFit import  validFilt
import scipy.signal as signal
from makeEvenOrientationCells import  makeEvenOrientationCells
def edgeEvenPyramid(map, params):


    orientation= {}
    orientation['data'] = []
    orientation['ori'] = []
    oris = []
    data = []

    prs = params['evenCellPrs']
    for l in range(prs['minLevel']-1,prs['maxLevel']):

        oris = []
        data = []


        for ori in range(prs['numOri']):
            Evmsk = makeEvenOrientationCells(prs['oris'][ori], prs['lamba'], prs['sigma'], prs['gamma'])

            oris.append(prs['oris'][ori])
            data.append(signal.correlate(map['data'][l], Evmsk,mode='same'))
        orientation['data'].append(data)
        orientation['ori'].append(oris)

            # newMap[l]['orientation'][ori]['ori'] =
            # newMap[l]['orientation'][ori]['data'] =





    return orientation