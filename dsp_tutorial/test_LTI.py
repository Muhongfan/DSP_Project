# -*- coding: utf-8 -*-
"""
Code illustrating how to do basic DSP operations in python with scipy, numpy, matplotlib: 
filtering, FFT/IFFT, PSD estimation, system identification, read/write to audio files, plots
"""

###################  main library imports #####################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from scipy import random
from scipy import io
import scipy.io.wavfile

###################  local imports or local definitions #######################

## The function zplane(b,a)  does not exist in the Python libraries, so we import it here.
from plot_zplane import zplane   # use a local file "plot_zplane.py" defining zplane()


###################  main program #############################################

plt.close('all') #关闭所有图
random.seed(1234)

signal_length=10000

# generate and display input random white gaussian noise
x = random.randn(signal_length) # will be 1D, unlike Matlab
X = fftpack.fft(x)
X = np.abs(X);
X= X*X/len(X)
#print(np.shape(x))
#print(np.shape(X))
nperseg=256
noverlap=nperseg/2
nfft=nperseg

#Estimate the cross power spectral density, Pxy, using Welch’s method.
freqtmp, Pxx = signal.csd(x, x, fs=1.0, window='hann', nperseg=nperseg, noverlap=noverlap, nfft=nfft,
   detrend=False, return_onesided=False, scaling='density', axis=-1) # csd() normalizes window rms value
freq=np.linspace(0, 1, nfft, False)
#print(np.shape(freq))
#print(np.shape(Pxx))

"""
n=np.linspace(0, signal_length-1, signal_length)
#print(np.shape(n))
#fig=plt.figure()
f, axarr = plt.subplots(3, sharex=False)

axarr[0].plot(n, x)
axarr[0].set_title('input signal x[n]')
axarr[0].set_ylabel('x')
axarr[0].set_xlabel('n')
axarr[0].grid()

axarr[1].plot(n, X)
axarr[1].set_title('FFT |X[k]|^2/N')
axarr[1].set_ylabel('X')
axarr[1].set_xlabel('k')
axarr[1].grid()

ylim = axarr[1].get_ylim()
ymin=ylim[0]
axarr[1].set_ylim([ymin,10]) # example adjusting the axis scale

axarr[2].plot(freq, Pxx)
axarr[2].set_title('PSD Pxx[f]')
axarr[2].set_ylabel('Pxx')
axarr[2].set_xlabel('f')
axarr[2].grid()

ylim = axarr[2].get_ylim()
ymax=ylim[1]
axarr[2].set_ylim([0,ymax]) # example adjusting the axis scale

plt.draw() 
plt.show()

"""
# generate and characterize LTI system

b, a = signal.iirfilter(4, Wn=0.2, rp=0.5, rs=60, btype='lowpass', ftype='ellip')
w, H = signal.freqz(b,a,512,True)
nh, h = signal.dimpulse([b,a,1], x0=None, t=None, n=nperseg) # same length as PSD estim, for comparison with hmodel
lenn=len(nh)
h=np.reshape(h,lenn,1)

#fig=plt.figure()
f, axarr = plt.subplots(2, sharex=False)
#axarr[0].plot(w, 20*np.log10(np.abs(H)))
"""
axarr[0].plot(w, np.abs(H))
axarr[0].set_title('LTI freq. response |H(w)|')
axarr[0].set_ylabel('H')
axarr[0].set_xlabel('w')
axarr[0].grid()
axarr[1].plot(nh, h)
#axarr[1].stem(nh, h, '-.')
axarr[1].set_title('LTI impulse response h[n]')
axarr[1].set_ylabel('h')
axarr[1].set_xlabel('n')
axarr[1].grid()
plt.draw() 
plt.show()

fig=plt.figure()
zplane(b,a)  # external plot_zplane.py file
plt.title('z-plane, poles and zeros of LTI H(z)')
plt.draw() 
plt.show() 
"""
# generate and display output signal

zi = signal.lfilter_zi(b, a)
y, zf = signal.lfilter(b, a, x, axis=-1, zi=zi)
Y = fftpack.fft(y)
Y = np.abs(Y);
Y = Y*Y/len(Y)
freqtmp, Pyy = signal.csd(y, y, fs=1.0, window='hann', nperseg=nperseg, noverlap=noverlap, nfft=nfft,
   detrend=False, return_onesided=False, scaling='density', axis=-1) # csd() normalizes window rms value

#fig=plt.figure()
f, axarr = plt.subplots(3, sharex=False)
"""
axarr[0].plot(n, y)
axarr[0].set_title('output signal y[n]')
axarr[0].set_ylabel('y')
axarr[0].set_xlabel('n')
axarr[0].grid()
axarr[1].plot(n, Y)
axarr[1].set_title('FFT |Y[k]|^2/N')
axarr[1].set_ylabel('Y')
axarr[1].set_xlabel('k')
axarr[1].grid()
axarr[2].plot(freq, Pyy)
axarr[2].set_title('PSD Pyy[f]')
axarr[2].set_ylabel('Pyy')
axarr[2].set_xlabel('f')
axarr[2].grid()
plt.draw() 
plt.show()

"""
# identify frequency response and impulse response from PSDs (system identification)

freqtmp, Pyx = signal.csd(x, y, fs=1.0, window='hann', nperseg=nperseg, noverlap=noverlap, nfft=nfft,
   detrend=False, return_onesided=False, scaling='density', axis=-1) # csd() normalizes window rms value
Hmodel= Pyx / Pxx
hmodel=np.real(fftpack.ifft(Hmodel))
#hmodel2=np.imag(fftpack.ifft(Hmodel))

f, axarr = plt.subplots(3, sharex=False)
"""
axarr[0].plot(freq, np.abs(Hmodel))
axarr[0].set_title('freq. resp. syst. identif. |Hmodel[f]|')
axarr[0].set_ylabel('Hmodel')
axarr[0].set_xlabel('f')
axarr[0].grid()
#axarr[1].stem(nh, hmodel, '-.')
axarr[1].plot(nh, hmodel)
axarr[1].set_title('imp. resp. syst. identif. hmodel[n]')
axarr[1].set_ylabel('hmodel')
axarr[1].set_xlabel('n')
axarr[1].grid()
#axarr[2].stem(n, h-hmodel, '-.')
axarr[2].plot(nh, h-hmodel)
axarr[2].set_title('error herr[n]')
axarr[2].set_ylabel('herr')
axarr[2].set_xlabel('n')
axarr[2].grid()
plt.draw() 
plt.show()

"""
# simple write and read of WAV files (16 bits integer 2's complement -32768 to 32767 values)
# unlike Matlab's floating point normalized values -1.0 to 1.0)

scaled = np.int16(x/np.max(np.abs(x)) * 32767) # 16 bits integer, and use full scale available
io.wavfile.write('x.wav', 8000, scaled)
scaled = np.int16(y/np.max(np.abs(y)) * 32767) # 16 bits integer, and use full scale available
io.wavfile.write('y.wav', 8000, scaled)
rate, xread = io.wavfile.read('x.wav') # 16 bits integer
xread=np.float64(xread) # 64 bits float
rate, yread = io.wavfile.read('y.wav') # 16 bits integer
yread=np.float64(yread) # 64 bits float

f, axarr = plt.subplots(2, sharex=False)
"""
axarr[0].plot(n, xread)
axarr[0].set_title('x[n] read')
axarr[0].set_ylabel('x')
axarr[0].set_xlabel('n')
axarr[0].grid()
axarr[1].plot(n, yread)
axarr[1].set_title('y[n] read')
axarr[1].set_ylabel('y')
axarr[1].set_xlabel('n')
axarr[1].grid()
plt.draw() 
plt.show()
"""
# simple read and write of MAT files

io.savemat('x.mat',mdict={'xread2':x}) # save variable x under the entry xread2 in file x.mat
io.savemat('y.mat',mdict={'yread2':y}) # save variable y under the entry yread2 in file y.mat
matread=io.loadmat('x.mat') 
xread2=matread['xread2']
matread=io.loadmat('y.mat')
yread2=matread['yread2']
# somehow the read arrays are 1 x signal length, instead of signal_length x 1
xread2=np.reshape(xread2,signal_length,1)
yread2=np.reshape(yread2,signal_length,1)

f, axarr = plt.subplots(2, sharex=False)
"""
axarr[0].plot(n, xread2)
axarr[0].set_title('x[n] read')
axarr[0].set_ylabel('x')
axarr[0].set_xlabel('n')
axarr[0].grid()
axarr[1].plot(n, yread2)
axarr[1].set_title('y[n] read')
axarr[1].set_ylabel('y')
axarr[1].set_xlabel('n')
axarr[1].grid()
plt.draw() 
plt.show()


"""