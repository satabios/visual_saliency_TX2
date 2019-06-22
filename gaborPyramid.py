

from makeEvenOrientationCells import makeEvenOrientationCells
from validFilt import validFilt
def gaborPyramid(pyr,ori,parms):

    data = []
    depth = parms['maxLevel']
    gaborPrs = parms['gaborPrs']

    Evmsk = makeEvenOrientationCells(ori,gaborPrs['lamba'],gaborPrs['sigma'],gaborPrs['gamma'])

    for l in range(depth):
        data.append(validFilt(pyr['data'][l],Evmsk))



    return