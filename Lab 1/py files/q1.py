import matplotlib.pyplot as plt
import numpy as np

def mysinplot(f, fs, n):
    omega = 1/fs
    samples = np.arange(-(fs*n)/2,(fs*n)/2 + 0.1, 1)
    w = 2 * np.pi * omega
    wave = np.sin(w * samples)
    time = samples/(fs*f)
    print("wave size: ", wave.size)
    plt.stem(time,wave)
    plt.title('Sine Wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True, which='both')
    plt.show()

frequency = int(input("Input Frequency: "))
sampling_frequency = int(input("Input Sampling Frequency: "))
cycles = int(input("Input number of cycles: "))
mysinplot(frequency,sampling_frequency,cycles)