import scipy.io as si
import numpy as np

def load_CIPIC_HRIR(hrir_fn,front,back,left_or_right):
    m=si.loadmat(hrir_fn)
    hrir_l=m["hrir_l"]
    hrir_r=m["hrir_r"]
    if left_or_right == 'left':
        #left ear
        out = np.flip(np.squeeze(hrir_l[:,front,:]),1)
        out_r = out[0:13,:]
        out_l = out[13:25,:]
        out = np.row_stack((out_l, np.squeeze(hrir_l[:, back,:])))
        out = np.row_stack((out,out_r))


    else:

        # right ear
        out = np.flip(np.squeeze(hrir_r[:, front, :]), 1)
        out_r = out[0:13, :]
        out_l = out[13:25, :]
        out = np.row_stack((out_l, np.squeeze(hrir_r[:, back, :])))
        out = np.row_stack((out, out_r))
        '''
        out = np.squeeze(hrir_r[:, front, :])
        out = np.row_stack((out, np.flip(np.squeeze(hrir_r[:, back, :]), 1)))
        '''

    len_out = int(np.size(out) / 200)

    return out,len_out