import numpy as np
from scipy import fftpack
from scipy import signal as sig



L = 64  # length of input signal
N = 8  # length of impulse response
P = 24  # length of segments


# generate input signal
m = sig.triang(L)
#print(m)
# generate impulse response
h = sig.triang(N)
print("---")
# overlap-save convolution
nseg = (L+N-1)//(P-N+1) + 1
#x = np.concatenate((np.zeros(N-1), m, np.zeros(P)))


a= [1,2,3]
b= [4,5,6]
x  = np.concatenate((a,np.zeros(4)),axis=0)
#print(np.zeros(4))

print(x)
a1= np.fft.fft(a)
print(a1)
b1=np.fft.fft(b)
print(b1)
yp_L = np.fft.ifft(np.multiply(a1,b1))
print(yp_L)
