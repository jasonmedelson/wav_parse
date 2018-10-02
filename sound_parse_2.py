from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from numpy import mean
def is_ding(data):
    if len(data) > 350:
        segment = data[:350]
    else:
        segment = data
    hold = -10000000
    count = 0
    begin = False
    cycles = []
    for x in range(len(segment)):
        if len(cycles) > 5 and cycles.count(17)<1:
            cycles = [0,0,0,0]
            break
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
    cycles = cycles[1:-1]
    onesix = cycles.count(16)
    oneseven = cycles.count(17)
    total = onesix+oneseven
    percent = total/(len(cycles)+1)
    average = mean(cycles)
    return average,cycles,percent


fs, data = read('B2B-1.wav')
data_size = len(data)
print(data_size)
print(fs)
index = 0
while index < len(data):
    if index%int(fs*30)==0:
        print("30 seconds", index//fs)
    value = data[index][0]
    if value > 1600 and value < 2400:
        test = data[index:index+351]
        resp, arr, percent = is_ding(test)
        if resp >=16 and resp <=17:
            if percent > 0.81:
                print(index//fs,"--- possible ding", percent,value)
                index += fs*5
    index +=11
    
    
#print(data[:100])
#plt.plot(data2[fs:fs*2])
#plt.ylabel("Amplitude")
#plt.xlabel("Time")
#plt.title("WavGraph")
#plt.show()

