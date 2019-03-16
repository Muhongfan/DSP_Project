import scipy.io as si
import numpy as np

def load_CIPIC_HRIR(hrir_fn,front,back,left_or_right):
    m=si.loadmat(hrir_fn)
    hrir_l=m["hrir_l"]
    hrir_r=m["hrir_r"]
    if left_or_right == 'L':
        #left ear
        out = np.squeeze(hrir_l[:,front,:])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_l[:, back,:]), 1)))
    elif left_or_right == 'l':
        out = np.squeeze(hrir_l[:, front, :])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_l[:, back, :]), 1)))

    elif left_or_right == 'left':
        out = np.squeeze(hrir_l[:, front, :])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_l[:, back, :]), 1)))

    elif left_or_right == 'Left':
        out = np.squeeze(hrir_l[:, front, :])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_l[:, back, :]), 1)))

    elif left_or_right == 'LEFT':
        out = np.squeeze(hrir_l[:, front, :])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_l[:, back, :]), 1)))

    else :
        out = np.squeeze(hrir_r[:, front, :])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_r[:, back, :]), 1)))

    return out