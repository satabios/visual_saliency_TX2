import numpy as np
def seperatePyr(pyr,m):
    pyr1 =[]
    pyr2 =[]
    # if (m==2):
    #
    #     pyr1=[]
    #     pyr2=[]
    #     for l in range(len(pyr)):
    #
    #
    #         pyr1[l][pyr1[l]<0] = 0
    #         pyr2[l][pyr2[l]<0] = 0
    #
    # else:
    #


    pyr1 = np.multiply(1,pyr)
    pyr2 = np.multiply(-1,pyr)


    for l in range(len(pyr)):


        pyr1[l][pyr1[l] < 0] = 0
        pyr2[l][pyr2[l] < 0] = 0










    return pyr1,pyr2