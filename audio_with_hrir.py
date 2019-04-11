# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
from scipy import signal as sig
from scipy.io import wavfile

def audio_conv(file, hrir_data):
    #read the audio file
    fs, InAudio = wavfile.read(file)

    #Audio = np.transpose([InAudio])
    hrir_data = hrir_data

    #print(InAudio)
    #print(InA)

    #get the length of the audio file
    duration = len(InAudio)
    #seg_nums:  how many segement will be played in a circle
    seg_nums = int(np.size(hrir_data,1)/2)

    #the num of padding zeros
    remainder = np.mod(duration, seg_nums)

    if remainder > 0 :
        padding_zeros = int(seg_nums - remainder)
        zeros= np.zeros(padding_zeros)
        InAudio = np.hstack((InAudio,zeros))

    InAudio = np.transpose([InAudio])
    #step of each segment
    step = int(len(InAudio)/seg_nums)


    #init segment piece
    segment_L = np.zeros((seg_nums,step))
    segment_R = np.zeros((seg_nums,step))

    #hrir_data=np.transpose(hrir_data)
    for i in range(seg_nums):
        Hrir_d=np.transpose(hrir_data[ : , 2 * 0 ])
        ans=InAudio[ step * 0 : step * (  1 )]
       # zi = sig.lfilter_zi(np.transpose(hrir_data[ : , 2 * i ]),1.)
        L = sig.lfilter(np.transpose(hrir_data[ : , 2 * i ]), 1.,InAudio[ step * i : step * ( i + 1 )], axis=0)
        R = sig.lfilter(np.transpose(hrir_data[ : , 2 * i + 1]), 1.,InAudio[ step * i : step * ( i + 1 )], axis=0)
        #length=np.size(L)
        #L_seg = np.size(segment_L)
        segment_L[i,:] = np.transpose(L)
        segment_R[i,:] = np.transpose(R)

    left = segment_L[0]
    right = segment_R[0]
    for i in range(1,seg_nums):
        left = np.hstack((left,segment_L[i]))
        right = np.hstack((right,segment_R[i]))

    #find max value
    max_value = np.max(np.abs(np.hstack((left,right))))

    #normalization
    left = left / max_value
    right = right / max_value

    #output
    out = np.transpose(np.vstack((left, right)))

    #normalization
    max_value = np.max(np.max(np.abs(out)))
    out = out / max_value

    return out

'''
    size = np.size(segment_L[0])
    win_end = int(size - (windows_N/2))
    win = int(windows_N/2)
    length=len(segment_L)
    
    
    #fade in and fade out
    for i in range(seg_nums):
        segment_L[i][0:win] = np.multiply(segment_L[i][0:win],window[0:win])
        segment_R[i][0:win] = np.multiply(segment_R[i][0:win],window[0:win])

        segment_L[i][win_end:size] = np.multiply(segment_L[i][win_end:size],window[win:size])
        segment_R[i][win_end:size] = np.multiply(segment_R[i][win_end:size],window[win:size])

    #step 1:  for the first segments, we dont need fade in at the beginning
    left = np.hstack((segment_L[1][0:win_end], segment_L[1][win_end:size] + segment_L[2][0:win]))
    right =np.hstack((segment_R[1][0:win_end], segment_R[1][win_end:size] + segment_R[2][0:win]))

    #step 2: for the rest segments,except the last
    for i in range(1,seg_nums-1):
        left = np.hstack((left, segment_L[i][win:win_end], segment_L[i][win_end:size] + segment_L[i+1][0:win]))
        right = np.hstack((right, segment_R[i][win:win_end], segment_R[i][win_end:size] + segment_R[i+1][0:win]))

    left = np.hstack((left, segment_L[seg_nums-1][win:size]))
    right = np.hstack((right, segment_R[seg_nums-1][win:size]))


'''
'''
    #filtering
    out_left = sig.lfilter(lowpass,1.,left)
    out_right = sig.lfilter(lowpass,1.,right)
    out_left = sig.lfilter(highpass,1.,out_left)
    out_right = sig.lfilter(highpass,1.,out_right)
'''

''' 
    win_N=windows_N/2
    left=[]
    right=[]
    s=[]
    win_end = len(segment_L) - win_N/2


    for m in range(seg_nums):
        for n in range(win_N/2):
            segment_L[m][n] = np.multiply(segment_L[m][n],window[n])
            segment_R[m][n] = np.multiply(segment_R[m][n],window[n])
        for k in range(win_end+1,len(segment_L)):
            for l in range((win_N/2)+1,win_N):
                segment_L[m][k] = np.multiply(segment_L[m][k],window[l])
                segment_R[m][k] = np.multiply(segment_R[m][k],window[l])



    for i in range(win_end+1,len(segment_L)):
        for j in range(win_N/2):
            s[1][j]=segment_L[1][j] + segment_L[2][p]
            left = np.append((segment_L[1][i],segment_L[1][j]+segment_L[2][i]))
            right = np.append((segment_R[1][i],segment_R[1][j],segment_R[2][i]))

    for m in range(1,seg_nums):
        left =

'''


















