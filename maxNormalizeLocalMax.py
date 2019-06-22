
from normalizeImage import  normalizeImage
# from skimage.feature import peak_local_max
import cv2
import numpy as np

def getLocalMaxima(data,thresh):

    refData = data [1:-1,1:-1]
    localMax = (np.logical_and.reduce((np.asarray(refData >= data[0:-2,1:-1]), \
                                       np.asarray(refData >= data[2:, 1:-1]), \
                                       np.asarray(refData >= data[1:-1, 0:-2]), \
                                       np.asarray(refData >= data[1:-1, 2:]), \
                                       np.asarray(refData >= thresh)))).astype(int)
    maxData = refData *np.squeeze(localMax)
    lm_avg = np.mean(maxData)
    lm_sum = np.sum(maxData)
    lm_num = len(np.asarray(maxData))

    return lm_avg, lm_num, lm_sum
#
# def SMRangeNormalize(self, src):
#     minn, maxx, dummy1, dummy2 = cv2.minMaxLoc(src)
#     if (maxx!= minn):
#         dst = src /(maxx -minn) + minn /(minn -maxx)
#     else:
#         dst = src - minn
#     return dst
#     ## computing an average of local maxima
# def SMAvgLocalMax(self, src):
#     # size
#     stepsize = pySaliencyMapDefs.default_step_local
#     width = src.shape[1]
#     height = src.shape[0]
#     # find local maxima
#     numlocal = 0
#     lmaxmean = 0
#     for y in range(0, heigh t -stepsize, stepsize):
#         for x in range(0, widt h -stepsize, stepsize):
#             localimg = src[y: y +stepsize, x: x +stepsize]
#             lmin, lmax, dummy1, dummy2 = cv2.minMaxLoc(localimg)
#             lmaxmean += lmax
#             numlocal += 1
#     # averaging over all the local regions
#     return lmaxmean / numlocal
#     ## normalization specific for the saliency map model
# def SMNormalization(self, src):
#     dst = self.SMRangeNormalize(src)
#     lmaxmean = self.SMAvgLocalMax(dst)
#     normcoeff = ( 1 -lmaxmean ) *( 1 -lmaxmean)
#     return dst * normcoeff
#     # normalizing feature maps
# def normalizeFeatureMaps(self, FM):
#     NFM = list()
#     for i in range(0 ,6):
#         normalizedImage = self.SMNormalization(FM[i])
#         # nownfm = cv2.resize(normalizedImage, (self.width, self.height), interpolation=cv2.INTER_LINEAR)
#         nownfm = cv2.resize(normalizedImage, self.width, self.height, interpolation=cv2.INTER_LINEAR)
#         NFM.append(nownfm)
#     return NFM


def maxNormalizeLocalMax(src,ran):

    data  = normalizeImage(src,ran)
    thres = 1
    lm_avg, lm_num, lm_sum = getLocalMaxima(data,thres)
    if(lm_num >1):
        result = data * (ran[1]**2)
    else:
        result = data

    return result