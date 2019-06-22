
import numpy as np

def makeComplexEdge(EPyr,OPyr):


    cmp_edge =[]
    for l in range(len(EPyr['data'])):

        cmp_edge.append(np.sqrt(np.square(EPyr['data'][l])+np.square(OPyr['data'][l])))


    return cmp_edge
