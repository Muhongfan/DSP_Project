# -*- coding: utf-8 -*-

'''
CHANGE THE LENGTH OF .wav FILE
'''
from pydub import AudioSegment
file_name = "275961__derjuli__birds.wav"
sound = AudioSegment.from_wav(file_name)
start_time = "0:00"
stop_time = "0:20"
print("time:",start_time,"~",stop_time)
start_time = (int(start_time.split(':')[0])*60+int(start_time.split(':')[1]))*1000
stop_time = (int(stop_time.split(':')[0])*60+int(stop_time.split(':')[1]))*1000
print("ms:",start_time,"~",stop_time)
word = sound[start_time:stop_time]
save_name = "word"+file_name[6:]
print(save_name)
word.export(save_name, format="wav",tags={'artist': 'AppLeU0', 'album': save_name[:-4]})
