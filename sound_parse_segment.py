from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
import math
from numpy import mean

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
fs, data = read('B2B-1.wav')
second = 1115
length = 1.7
#length = 0.11 #101
segment = data[fs*second:math.floor(fs*(second+length))]
print('starting')
write('testding.wav',fs,segment)
#print(segment[:100])
print('done')
if segment in data:
    print("true")
else:
    print("false")
hold = -10000000
count = 0
begin = False
print(is_ding(segment))

plt.plot(segment)
plt.ylabel("Amplitude")
plt.xlabel("Time")
title = "WavGraph"+ str(second)
plt.title(title)
plt.show()

