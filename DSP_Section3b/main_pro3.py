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
    sin = np.sin(m*np.pi/180)
    a = (1+sin)/2
    T_r = (1-a)*t
    T_l = a * t
    for n,k in enumerate(range(-100,100)):
        w = (2 * k * np.pi) / 200 * 44100
        H_r[n] = (1 + (2 * a * w * t) * 1j) / (1 + (w * t) * 1j) * np.exp(-(w * T_r) * 1j)
        H_l[n] = (1 + (2 * (1 - a) * w * t) * 1j) / (1 + (w * t) * 1j) * np.exp(-(w * T_l) * 1j)

        right = np.fft.ifft(np.fft.fftshift(H_r))
        H_r = np.fft.ifftshift(right)

        left = np.fft.ifft(np.fft.fftshift(H_l))
        H_l = np.fft.ifftshift(left)

        test_l = H_l
        test_r = H_r
        Hrir[2 * i, :] = H_r
        Hrir[2 * i + 1, :] = H_l

Hrir=np.transpose(Hrir)
#conv
out = audio_conv(file,Hrir)
#out3 = audio_test(file,hrir)

#audio write
out=np.int16( out* 32767)
wavfile.write('Horizontal_pro3.wav',44100,out)
