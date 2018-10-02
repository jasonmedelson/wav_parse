from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt

fs, data = read('B2B-1.wav')
seconds = [101,115,179,357]
length = 2
print('starting')
for second in seconds:
    segment = data[fs*second:fs*(second+length)]
    plt.plot(segment)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    title = "WavGraph"+ str(second)
    plt.title(title)
    plt.show()
print('done')
