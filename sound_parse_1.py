from scipy.io.wavfile import read
import matplotlib.pyplot as plt
fs, data = read('ding.wav')
fs2, data2 = read('B2B-1.wav')
data_size = len(data)
print(data_size)
print(fs)
dmax = 0
maxid = 0
minid = 0
dmin = 0
for num in range(len(data)):
    if data[num][0]>dmax:
        dmax = data[num][0]
        maxid = num
    if data[num][0]<dmin:
        dmin = data[num][0]
        minid = num
print(dmax,dmin)
print(maxid,minid)
print(data[minid:maxid+1])
#for num in range(len(data2)):
#    if data2[num][0] == dmin:
#        print("min found",num//fs)
#        if data2[num+17][0] == dmax:
#            print("found",num//fs)
#        if data2[num+17][0] > 0:
#            print(data2[num:num+18])
for num in range(len(data2)):
    if data2[num][0] == data[maxid][0]:
        print("max found",num//fs)
        if data2[num][1] == data[maxid][1]:
            print("found",num//fs)
#print(data[:100])
#plt.plot(data2[fs:fs*2])
#plt.ylabel("Amplitude")
#plt.xlabel("Time")
#plt.title("WavGraph")
#plt.show()
