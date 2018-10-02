from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from numpy import mean
fs, data = read('B2B-1.wav')
data_size = len(data)
print(data_size)
print(fs)
index = 0
while index < len(data):
    if index%(fs*30)==0:
        print("30 seconds")
    value = data[index][0]
    if value > 1600 and value < 2400:
        test = data[index:index+170]
        resp = is_ding(test)
        if resp >=16 and resp <=17:
            print(index//fs,"--- possible ding")
            index += fs*3
    
    
#print(data[:100])
#plt.plot(data2[fs:fs*2])
#plt.ylabel("Amplitude")
#plt.xlabel("Time")
#plt.title("WavGraph")
#plt.show()

def is_ding(data):
    if len(data) > 170:
        segment = data[:170]
    else:
        segment = data
    hold = -10000000
    count = 0
    begin = False
    cycles = []
    for x in range(len(segment)):
        item = segment[x][0]
        if item < hold:
            if not begin:
                cycles.append(count)
                count = 0
                begin = True
        if item > hold:
            begin = False
        hold = item
        count += 1
    cycles = cycles[1:]
    cycles = mean(cycles)
    return cycles
