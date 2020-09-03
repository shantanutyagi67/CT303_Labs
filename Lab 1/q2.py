import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft,fftfreq

def myctft(T,T1,fs):
    f = 10;
    time_x = np.arange(-T,T + 1/(fs*f), 1/(fs*f))
    x = np.sin(2 * np.pi * f * time_x)
    time_y = np.arange(-T1, T1 + 1 / (fs * f), 1 / (fs * f))
    if T1 <= T:
        y = np.sin(2 * np.pi * f * time_y)
    else:
        y = x
        num = int((time_y.size - time_x.size)/2);
        zero_arr = np.zeros(num);
        y = np.concatenate((zero_arr,y), axis = 0)
        y = np.concatenate((y,zero_arr), axis = 0)
    y_fft = 2*abs(fft(y))/time_y.size
    freq = fftfreq(time_y.size,1/(f*fs))

    plt.figure(1)
    plt.plot(time_x, x)
    plt.title('x(t) = sin(2*pi*f*t)')
    plt.xlabel('Time')
    plt.ylabel('x(t)')
    plt.grid(True, which='both')
    plt.show()

    plt.figure(2)
    plt.plot(time_y, y)
    plt.title('y(t) = sin(2*pi*f*t)')
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.grid(True, which='both')
    plt.show()

    plt.figure(3)
    plt.plot(freq, y_fft)
    plt.title('Amplitude Spectrum of y')
    plt.xlabel('Frequency')
    plt.ylabel('Y(jw)')
    plt.grid(True, which='both')
    plt.show()


T = float(input("Input T: "))
T1 = float(input("Input T1: "))
fs = float(input("Input sampling frequency: "))
#f = float(input("Input frequency: "))
myctft(T,T1,fs)