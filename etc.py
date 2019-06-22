
def calcSigma(r, x):
    sigma1 = r ^ 2 / (4 * np.log(x)) * (1 - 1 / x ^ 2)
    sigma1 = np.sqrt(sigma1)
    sigma2 = x * sigma1

    return sigma1, sigma2


def meshgrid(x, y, z):
    xrow = x  # % Make sure x is a full row vector.
    ycol = y  # % Make  sure y is a full column     vector. \
    xx = mat.repmat(xrow, len(ycol))
    yy = mat.repmat(ycol, len(xrow))  # 7*7

    return xx, yy


def makeGauss(dim1, dim2, sigma_1, sigma_2, theta, x0, y0, norm, *args):
    x0 = 0
    y0 = 0

    norm = 1

    msk = np.zeros((np.shape(dim1)[0], np.shape(dim1)[1]))
    [X, Y] = meshgrid(dim1, dim2)  # stopped here  ; )
    a = math.cos(theta) ^ 2 / 2 / sigma_1 ^ 2 + math.sin(theta) ^ 2 / 2 / sigma_2 ^ 2
    b = -math.sin(2 * theta) / 4 / sigma_1 ^ 2 + math.sin(2 * theta) / 4 / sigma_2 ^ 2
    c = math.sin(theta) ^ 2 / 2 / sigma_1 ^ 2 + math.cos(theta) ^ 2 / 2 / sigma_2 ^ 2

    if norm:

        msk = 1 / ((2 * math.pi * sigma_1 * sigma_2) * np.exp(
            - (a * (X - x0) ^ 2 + 2 * b * (X - x0) * (Y - y0) + c * (Y - y0) ^ 2)))
    else:
        msk = math.exp(- (a * (X - x0) ^ 2 + 2 * b * (X - x0) * (Y - y0) + c * (Y - y0) ^ 2));

    return msk


def makeCentreSurround(std_center, std_surround):
    center_dim = np.ceil(3 * std_center)
    surround_dim = np.ceil(3 * std_surround)

    idx_center = [dim for dim in range(-center_dim, center_dim + 1)]
    idx_surround = [dim for dim in range(-surround_dim, 1 + surround_dim)]
    msk_center = makeGauss(idx_center, idx_center, std_center, std_center, 0);
    msk_surround = makeGauss(idx_surround, idx_surround, std_surround, std_surround, 0);

    msk = -msk_surround
    msk[(surround_dim + 1 - center_dim): (surround_dim + 1 + center_dim), (surround_dim + 1 - center_dim): (
            surround_dim + 1 + center_dim)] = msk[(surround_dim + 1 - center_dim): ( \
                surround_dim + 1 + center_dim), (surround_dim + 1 - center_dim): ( \
                surround_dim + 1 + center_dim)] + msk_center
    msk = msk - (np.sum(np.sum(msk))) / ((np.shape(msk)[0]) * (np.shape(msk)[1]))

    return msk


def makeDefaultParams(w):
    minLevel = 1
    maxLevel = 10

    downSample = 'half'

    params = {}

    params['channels'] = 'ICO'
    params['maxLevel'] = maxLevel

    ori = [0, 45]
    oris = np.gradient([ori, ori + 90])

    [sigma1, sigma2] = calcSigma(2, 3)

    params['csPrs']['inner'] = sigma1
    params['csPrs']['inner'] = sigma2
    params['csPrs']['depth '] = maxLevel
    params['csPrs']['downSample'] = downSample

    start = time.time()
    msk = makeCentreSurround(params['csPrs']['inner'], params['csPrs']['inner'])
    temp = msk[round(len(msk, 1) / 2), :]

    temp[temp > 0] = 1
    temp[temp < 0] = -1
    zc = temp[round(len(msk, 2) / 2):] - temp[round(len(msk, 1) / 2) + 1:]
    R0 = np.where(abs(zc) == 2)
    print('\nCenter Surround Radius is %d pixels. \n', R0)

    print(time.time() - start, '\n')

    params['gaborPrs']['lamba'] = 8
    params['gaborPrs']['sigma'] = 0.4 * params['gaborPrs']['lamba']
    params['gaborPrs']['gamma'] = 0.8

    params['evenCellPrs']['minLevel'] = minLevel
    params['evenCellPrs']['maxLevel'] = maxLevel
    params['evenCellPrs']['oris'] = oris
    params['evenCellPrs']['numOri'] = len(oris)
    params['evenCellPrs']['lamba'] = 4
    params['evenCellPrs']['sigma'] = 0.56 * params['evenCellPrs']['lamba']
    params['evenCellPrs']['gammaa'] = 0.5

    params['oddCellPrs']['minLevel'] = minLevel
    params['oddCellPrs']['maxLevel'] = maxLevel
    params['oddCellPrs']['oris'] = oris
    params['oddCellPrs']['numOri'] = len(oris)
    params['oddCellPrs']['lamba'] = 4
    params['oddCellPrs']['sigma'] = 0.56 * params['evenCellPrs']['lamba']
    params['oddCellPrs']['gammaa'] = 0.5

    params['bPrs']['inLevel'] = minLevel
    params['bPrs']['axLevel'] = maxLevel
    params['bPrs']['numOri'] = len(oris)
    params['bPrs']['alpha'] = 1
    params['bPrs']['oris'] = oris
    params['bPrs']['CSw'] = 1

    params['vmPrs']['minLevel'] = minLevel
    params['vmPrs']['maxLevel'] = maxLevel
    params['vmPrs']['oris'] = oris
    params['vmPrs']['numOri'] = len(oris)
    params['vmPrs']['R0'] = R0

    params['giPrs']['w_sameChannel'] = 1

    params['tPrs']['w'] = w

    return params


def makeTemporalFilter(params):
    alpha = -0.000487
    beta = -0.000466
    tau = 116
    delta = 20
    tmax = 250
    dt = 24

    if (params == 'strong_t3'):
        alpha = -0.00161;
        beta = -0.00111;
        tau = 86.2;
        delta = 5.6;
        tmax = 250;
        dt = 12;


    else:
        alpha = -0.000487;
        beta = -0.000466;
        tau = 116;
        delta = 20;
        tmax = 250;
        dt = 24;

    tstep = 1 / (dt * 1000);
    print(tstep)
    t = [i for i in range(1, tmax)];
    t = np.asarray(t)

    rc = alpha * (t - tau - delta) * np.exp(beta * (t - tau) ** 2);
    r = np.zeros((1, 1, 1, 3))
    ;
    for i in range(int(250 / tstep)):
        r[i] = np.sum(rc[(i - 1) * tstep + 1:i * tstep]);

    r = r / np.sum(np.sum(r > 0));

    if (params != 'weak_t6'):
        r = r - mean(r);

    return r





# [batch, in_depth, in_height, in_width, in_channels].   []
# [filter_depth, filter_height, filter_width, in_channels, out_channels]


f = makeTemporalFilter('strong_t3')

frames = tf.constant(np.ones((1, 320, 204, 201, 3)))

a = tf.reshape(frames, [3, 204, 320, 201, 1])

fil = tf.to_double(tf.constant(np.reshape(f, [3, 1, 1, 1, 1])))

cn = tf.nn.conv3d(
    filter,
    fil,
    strides=[1, 1, 1, 1, 1],
    padding='SAME'

)

tf.shape(cn)