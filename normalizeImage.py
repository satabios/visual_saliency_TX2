import tensorflow as tf

def normalizeImage(*frame):

    if(len(frame)<=1):
        rn =[0,1]
    else:
        rn = frame[1]

    mx = tf.reduce_max(frame[0])
    mn = tf.reduce_min(frame[0])
    frame = tf.divide(tf.subtract(frame[0], mn), tf.subtract(mx, mn)) * abs(rn[1]-rn[0]) + min(rn)


    return frame