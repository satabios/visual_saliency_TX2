
import  numpy as np

def calcSigma(r, x):
    sigma1 = r ** 2 / (4 * np.log(x)) * (1 - 1 / x ** 2)
    sigma1 = np.sqrt(sigma1)
    sigma2 = x * sigma1

    return sigma1, sigma2
