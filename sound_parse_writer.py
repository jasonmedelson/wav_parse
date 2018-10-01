from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt


fs2, data2 = read('B2B-1.wav')

segment=data2[:fs2*5]
write("test.wav",fs2,segment)
