import matplotlib.pyplot as plt
import numpy as np

def mysinplot(f, fs, n):
    x = np.linspace(-n/(2*f),n/(2*f),fs*n)
    plt.stem(x,np.sin(2*np.pi*f*x))
    plt.title('Sine Wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True, which='both')
    plt.show()

wave_frequency = int(input("Input Frequency: "))
sampling_frequency = int(input("Input Sampling Frequency: "))
no_cycles = int(input("Input number of cycles: "))
mysinplot(wave_frequency,sampling_frequency,no_cycles)