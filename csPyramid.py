
from makeCentreSurround import makeCentreSurround
from validFilt import validFilt
import numpy as np

def csPyramid(pyr,params):

    depth = params['maxLevel']
    csPrs = params['csPrs']
    data= []

    CSmsk = makeCentreSurround(csPrs['inner'],csPrs['outer'])

    for l in range(depth):
        data.append(validFilt(np.asarray(pyr['data'][l]),CSmsk))

    return data







