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


a= [1,2,3,4,4,3,2,1]
b= [1,2,3,4]
c=[4,3,2,1]
d=[4,3,2,1,1,2,3,4]
#x  = np.concatenate((a,np.zeros(4)),axis=0)
#print(np.zeros(4))

#print(x)
a1= np.fft.ifft(a)
print(a1)
b1=np.fft.ifft(b)
print(b1)
c1=np.fft.ifft(c)
print(c)
d1=np.fft.ifft(d)
print(d1)

for i in range(-100,100):
    print(len(range(-100,100)))




