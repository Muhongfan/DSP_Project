###################  main library imports #####################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from scipy import random
from scipy import io
from scipy.io import wavfile
from scipy import signal as sig

###################  local imports or local definitions #######################
from audio_with_brir import audio_conv
from load_CIPIC_HRIR import load_CIPIC_HRIR

###################  main program #############################################

plt.close('all')

file = 'nokia.wav'
fs = 44100
hrir_fn= 'hrir_final.mat'
front = 9
back = 41

hrir_l = load_CIPIC_HRIR(hrir_fn,front,back,'left')
hrir_r = load_CIPIC_HRIR(hrir_fn,front,back,'right')

hrir_l=np.transpose(hrir_l)
hrir_r=np.transpose(hrir_r)


#get the total HRIR

hrir=np.array(np.zeros((200,100)))

#size=np.size(hrir_l,0)
#print(size)
for i in range(np.size(hrir_l,1)):
    hrir[:,i*2] = hrir_l[:,i]
    hrir[:,i*2+1] =  hrir_r[:,i]

#conv
out = audio_conv(file,hrir)

#audio write

out=np.int16(out* 32767)
wavfile.write('nokia_hrir5.wav',fs,out)