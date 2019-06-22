#
#
#
# import numpy as np
# import time
#
# import scipy.signal as signal
# import numpy
#
# # from numba import vectorize,cuda
#
# # @vectorize(['float32(float32,float32)'],target='cuda')
# def con(frames,r):
#     # st = time.time()
#     fil = signal.convolve(frames,r,mode='same')
#     # print(time.time()-st)
#     return fil
#

# import pycuda.autoinit
# import pycuda.driver as drv
# import numpy
#
# from pycuda.compiler import SourceModule
# mod = SourceModule("""
# __global__ void multiply_them(float *dest, float *a, float *b)
# {
#   const int i = threadIdx.x;
#   dest[i] = a[i] * b[i];
# }
# """)
#
# multiply_them = mod.get_function("multiply_them")
#
# a = numpy.random.randn(400).astype(numpy.float32)
# b = numpy.random.randn(400).astype(numpy.float32)
#
# dest = numpy.zeros_like(a)
# multiply_them(
#         drv.Out(dest), drv.In(a), drv.In(b),
#         block=(400,1,1), grid=(1,1))
#
# print (dest-a*b)
import tensorflow as tf

def _centered(arr, newshape):
    # Return the center newshape portion of the array.
    currshape = tf.shape(arr)[-2:]
    startind = (currshape - newshape) // 2
    endind = startind + newshape
    return arr[..., startind[0]:endind[0], startind[1]:endind[1]]

def fftconv(in1, in2, mode="full"):
    # Reorder channels to come second (needed for fft)
    # in1 = tf.transpose(in1, perm=[0, 3, 1, 2])
    # in2 = tf.transpose(in2, perm=[0, 3, 1, 2])

    # Extract shapes
    s1 = tf.convert_to_tensor(tf.shape(in1)[-2:])
    s2 = tf.convert_to_tensor(tf.shape(in2)[-2:])
    shape = s1 + s2 - 1

    # Compute convolution in fourier space
    sp1 = tf.spectral.rfft2d(in1, shape)
    sp2 = tf.spectral.rfft2d(in2, shape)
    ret = tf.spectral.irfft2d(sp1 * sp2, shape)

    # Crop according to mode
    if mode == "full":
        cropped = ret
    elif mode == "same":
        cropped = _centered(ret, s1)
    elif mode == "valid":
        cropped = _centered(ret, s1 - s2 + 1)
    else:
        raise ValueError("Acceptable mode flags are 'valid',"
                         " 'same', or 'full'.")

    # Reorder channels to last
    result = tf.transpose(cropped, perm=[0, 2, 3, 1])
    return result