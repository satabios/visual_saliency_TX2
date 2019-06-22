
import numpy as np
import math
def makeTemporalFilter(params):
    alpha = -0.000487
    beta = -0.000466
    tau = 116
    delta = 20
    tmax = 250
    dt = 24

    if (params == 'strong_t3'):
        alpha = -0.00161
        beta = -0.00111
        tau = 86.2
        delta = 5.6
        tmax = 250
        dt = 12


    else:
        alpha = -0.000487
        beta = -0.000466
        tau = 116
        delta = 20
        tmax = 250
        dt = 24

    tstep = 1 / dt * 1000
    print(tstep)
    t = [i for i in range(1, tmax+1)]
    t = np.asarray(t)

    rc = alpha * (t - tau - delta) * np.exp(beta * (t - tau) ** 2)

    if (params == 'weak_t6'):
        r = np.zeros((1, 1, 1, 6))
    else:
        r = np.zeros((1, 1, 1, 3))
    
    for i in range(int(250 / tstep)):
        r[:,:,:,i] = np.sum(rc[int(i * tstep) :int((i+1) * tstep)])

    r = r / np.sum(np.sum(r > 0))

    if (params != 'weak_t6'):
        r = r - np.mean(r)

    return r