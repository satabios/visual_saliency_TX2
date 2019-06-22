

from makePyramid import makePyramid
from edgeEvenPyramid import  edgeEvenPyramid
from edgeOddPyramid import edgeOddPyramid
from makeComplexEdge import  makeComplexEdge
from gaborPyramid import gaborPyramid
from seperatePyr import seperatePyr
from normCSPyr2 import normCSPyr2
from csPyramid import csPyramid
from borderPyramid import borderPyramid
from sumPyr import sumPyr

def makeBorderOwnership(img,params):

    # I =
    b1Pyr = []

    for m in range(len(img)):

        # print('\nAssigning Border Ownership on ')

        for sub in range(len(img[m]['subtype'])):

            map = img[m]['subtype'][sub]['data']
            imPyr = makePyramid(map, params)

            EPyr = edgeEvenPyramid(imPyr, params)
            OPyr = edgeOddPyramid(imPyr, params)
            cPyr = makeComplexEdge(EPyr,OPyr)

            if(m==2):
                csPyr = gaborPyramid(imPyr,img[m]['subtype'][sub]['ori'],params)

            else:
                csPyr = csPyramid(imPyr,params)

            csPyrL, csPyrD = seperatePyr(csPyr,m)
            csPyrL, csPyrD = normCSPyr2(csPyrL,csPyrD,m)

            bPyr1_1,bPyr1_2 = borderPyramid(csPyrL, csPyrD, cPyr, params)
            b1Pyr = sumPyr(bPyr1_1, bPyr1_2)










    return EPyr
    # return b1Pyr, b2Pyr