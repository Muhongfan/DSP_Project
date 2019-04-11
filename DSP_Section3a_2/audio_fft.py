# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as plt
from scipy import signal as sig
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
def audio_test(file, hrir_data):
    #read the audio file
    fs, InAudio = wavfile.read(file)

    #Audio = np.transpose([InAudio])
    hrir_data = hrir_data

    #print(InAudio)
    #print(InA)

    #get the length of the audio file
    #duration = len(InAudio)
    #seg_nums:  how many segement will be played in a circle
    seg_nums = int(np.size(hrir_data,1)/2)


    #step of each segment
    step = int(len(InAudio)/seg_nums)

    L = step
    P = int(L/2)
    hrir_data_L=np.zeros((200,50))
    hrir_data_R=np.zeros((200,50))

    #hrir_data=np.transpose(hrir_data)

    for i in range(seg_nums):
        hrir_data_L[:, i] = hrir_data[:, 2 * i]
        hrir_data_R[:, i] = hrir_data[:, 2 * i + 1]

    N_L = len(hrir_data_L)
    N_R = len(hrir_data_R)
    s=int(seg_nums*L//P)
    # overlap-add convolution
    xp = np.zeros((L // P, P + N_L -1))
    yp_L = np.zeros((L // P, N_L + P - 1))
    yp_R = np.zeros((L // P, N_R + P - 1))

    y_L = np.zeros(L + P - 1)
    y_R = np.zeros(L + P - 1)

    # init segment piece
    segment_L = np.zeros((seg_nums, step+N_L))
    segment_R = np.zeros((seg_nums, step+N_R))

    for i in range(seg_nums):
        for n in range(L // P):
        # M = InAudio[n * P:(n + 1) * P]
            xp = np.transpose(InAudio[(2*i+n) * P:(2*i+n+1) * P])
        #n = xp

            fft_audio = fft(xp,P + N_L -1)
            fft_hrir_L = fft(hrir_data_L[:, i ],P + N_L -1)
            fft_hrir_R = fft(hrir_data_R[:, i ],P + N_L -1)

            multipy_L = np.multiply(fft_audio,fft_hrir_L)
            multipy_R = np.multiply(fft_audio,fft_hrir_R)

            yp_L[n, :] = ifft(multipy_L)
            yp_R[n, :] = ifft(multipy_R)

            y_L[n * P:(n + 1) * P + N_L - 1] += yp_L[n, :]
            y_R[n * P:(n + 1) * P + N_R - 1] += yp_R[n, :]

        segment_L[i, :] = y_L[0:N_L + L]
        segment_R[i, :] = y_R[0:N_R + L]

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