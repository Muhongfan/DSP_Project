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
from audio_with_hrir import audio_conv
from load_CIPIC_HRIR import load_CIPIC_HRIR
from audio_fft import audio_test

###################  main program #############################################

#plt.close('all')

file = 'audio_pro.wav'

c = 340
t = (1.0/c)/2
Hrir = np.zeros((100,200))
H_r = np.zeros(200)
H_l = np.zeros(200)

test_l = np.zeros((50,200))
test_r = np.zeros((50,200))
for i in range(0,50):
    m = 360 - (7.2 * i)
    sin = np.sin(m)
    a = (1+sin)/2
    T_r = (1-a)*t
    T_l = a * t
    for n,k in enumerate(range(-100,100)):
        w = (2 * k * np.pi) / 200 * 44100
        H_r[n] = np.abs((1 + (2 * a * w * t) * 1j) / (1 + (w * t) * 1j) * np.exp(-(w * T_r) * 1j))
        H_l[n] = np.abs((1 + (2 * (1 - a) * w * t) * 1j) / (1 + (w * t) * 1j) * np.exp(-(w * T_l) * 1j))

        flipr_r = H_r[0:100]
        flipr_l = H_r[100:len(H_r)+1]
        right = np.abs(np.fft.ifft(np.concatenate((flipr_l, flipr_r), axis=0)))
        flipr_r = right[0:100]
        flipr_l = right[100:len(H_r)+1]
        H_r = np.concatenate((flipr_l, flipr_r), axis=0)

        flipl_r = H_r[0:100]
        flipl_l = H_r[100:len(H_l)+1]
        left = np.abs(np.fft.ifft(np.concatenate((flipl_l, flipl_r), axis=0)))
        flipl_r = left[0:100]
        flipl_l = left[100:len(H_l)+1]
        H_l = np.concatenate((flipl_l, flipl_r), axis=0)

        test_l = H_l
        test_r = H_r
        Hrir[2 * i, :] = H_r
        Hrir[2 * i + 1, :] = H_l

#conv
out = audio_conv(file,Hrir)
#out3 = audio_test(file,hrir)

#audio write
out=np.int16( out* 32767)
wavfile.write('Horizontal_pro3.wav',44100,out)