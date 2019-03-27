import scipy.io as si
import numpy as np

def load_CIPIC_HRIR_Vertical(hrir_fn,front,left_or_right):
    m=si.loadmat(hrir_fn)
    hrir_l=m["hrir_l"]
    hrir_r=m["hrir_r"]
    if left_or_right == 'left':
        # left ear
        out = np.squeeze(hrir_l[:, front, :])
        #out = np.row_stack((out, np.squeeze(hrir_l[:,back, :])))
        #out = np.row_stack((out, out1))

    else:
        out = np.squeeze(hrir_r[:, front, :])
        #out1 = out_r[0:13, :]
        # out2 = np.squeeze(hrir_l[12:24, front, :])
        #out2 = out_r[13:25, :]

        #out1 = np.flip(np.squeeze(hrir_r[0:13, front, :]), 1)
        # out2 = np.squeeze(hrir_l[12:24, front, :])
        # out2 = np.flip(np.squeeze(hrir_r[13:25, front, :]), 1)
        #out = np.row_stack((out2, np.squeeze(hrir_r[:, back, :])))
        #out = np.row_stack((out, out1))

    len_out = int(np.size(out) / 200)
    '''
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

    '''
    return out,len_out