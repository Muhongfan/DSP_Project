import numpy
import scipy.io as si


m=si.loadmat('/Users/momo/Documents/mhf/dsp_test/com/test_hrir.mat')
print(m)




'''
hrir_l=m["hrir_l"]

hrir_r=m["hrir_r"]

m1=si.loadmat('/Users/momo/Documents/mhf/dsp_test/com/test_hrir.mat')
print(m1)

'''




'''
arr = numpy.arange(9)
arr = arr.reshape((3, 3))  # 2d array of 3x3
print(arr)

si.savemat('/Users/momo/Documents/mhf/dsp_test/com/arrdata.mat', mdict={'arr': arr})
'''
