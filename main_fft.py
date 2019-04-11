###################  main library imports #####################################
import numpy as np
#import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from scipy import random
from scipy import io
from scipy.io import wavfile
from scipy import signal as sig
import scipy.io as si

###################  local imports or local definitions #######################
#from com.audio_with_brir import audio_conv
from load_CIPIC_HRIR_VERTICAL import load_CIPIC_HRIR_Vertical
#from load_CIPIC_HRIR import load_CIPIC_HRIR
from audio_fft import audio_test
###################  main program #############################################

#plt.close('all')

file = 'audio_pro.wav'
fs = 44100
hrir_fn= 'hrir_final.mat'

# Horizontal
#front = 8
#back = 40

# Vertical
front = 24
#back = 40

'''
hrir_l , len1= load_CIPIC_HRIR(hrir_fn,front,back,'left')
hrir_r , len2 = load_CIPIC_HRIR(hrir_fn,front,back,'right')

'''

hrir_l , len1= load_CIPIC_HRIR_Vertical(hrir_fn,front,'left')
hrir_r , len2 = load_CIPIC_HRIR_Vertical(hrir_fn,front,'right')

hrir_l=np.transpose(hrir_l)
hrir_r=np.transpose(hrir_r)

#get the total HRIR
hrir=np.array(np.zeros((200,int(len1*2))))

#size=np.size(hrir_l,0)
#print(size)
for i in range(np.size(hrir_l,1)):
    hrir[:,i*2] = hrir_l[:,i]
    hrir[:,i*2+1] =  hrir_r[:,i]

#conv
out = audio_test(file,hrir)

#audio write
out=np.int16( out* 32767)
wavfile.write('vertical.wav',fs,out)