
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from scipy import random
from scipy import io
from scipy.io import wavfile
from scipy import signal as sig
"""
hrir_data=[1,2,3,4,5,6,7,8,9]
hrir=[2,2,2,2,2,2,2,2,2,2]
InAudio=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sampFreq, snd = wavfile.read('nokia.wav')
#print (snd)


seg_nums=4
step=3
segment_L = np.array(np.zeros((seg_nums, step)))
segment_R = np.zeros((seg_nums, step))
#num=segment_L[1,1]
#print(np.dtype(num))
#print(segment_R)
for i in range(1,seg_nums):
    L = sig.lfilter([hrir_data[2 * i - 2]], 1., InAudio[step * (i - 1) :step * i])
   # print(L)
    R = sig.lfilter([hrir_data[2 * i - 1]], 1., InAudio[step * (i - 1):step * i])
    #for m in range(seg_nums):
    segment_L[i] = L

    #segment_R[m] = R
    #print(segment_L)
    #print(segment_R)

#print(segment_L)
#print(segment_R)



a=np.array([[7,5,7,2],[42,54,45,43],[10,8,15,14]])
b=np.array([[1,2,3,4],[5,6,7,8]])
c=np.array([[1,1,1],[2,2,2],[3,3,3]])
m=np.hstack((b[0],c[0]))
m=np.abs(m)
max_value = np.max(m)
b=b/max_value
print(b)

mmp=[]
mmp=np.array(mmp)
print(mmp)


print(np.append(a[0],b[1]))
print(np.hstack((a[1],b[1],a[0])))
print(a)
print(a[0][0:2]+b[0][2:4])
print(a[1,2])
print(a[1][1:3])
print(a[:,2])
print(a[2,:])

#c = [1,2]
#d = [0,1]
#b = a[c]
#b = b[:,d]
#print(b)
b=zeros((2,3))
print(b)
b[0]=[1,2,3]
print(b)
print(b[:,0])


import scipy.io as si
import numpy as np

m=si.loadmat('hrir_final.mat')
#print(m)
#m["labels"][0][0]
#print(m.keys())
#print(m[])

r=m["hrir_r"]
print(r)

print(type(m["hrir_r"]))
print(np.size(np.transpose(r),2))


for i in range(3):
    print(i)
"""


a=np.array([[7,5,7,2],[42,54,45,43]])
b=np.array([[1,2,3,4],[5,6,7,8]])
c=np.array([[1],[2],[3]])
hrir_data=[1,2,3,4,5,6,7,8,9]
h=np.transpose(hrir_data)
zeros= np.zeros(4)
a_=np.hstack((h,zeros))
answer=np.multiply(a,b)
answer2=a+b
print(a[1])
#print(a_)
d=sig.lfilter(np.transpose(hrir_data),1.,c)
#print(d)

e=np.append(hrir_data,np.zeros(1))
#print(e)
