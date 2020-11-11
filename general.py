from scipy.signal import butter, buttord, filtfilt
import numpy as np
import matplotlib.pyplot as plt


def cplot(ax, t, s, xl, yl, tit):
    ax.plot(t, s)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.set_title(tit)
    ax.grid(True)


def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = 2*cutoff / fs
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y


def butter_bandpass_filter(data, cutoff, fs, order):
    lfc, hfc = cutoff
    normal_cutoff = [2*lfc / fs, 2*hfc/fs]
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='band', analog=False)
    y = filtfilt(b, a, data)
    return y


def MSE(m1, m2):
    sum = 0
    for i in range(len(m1)):
        tmp = 0
        for j in range(len(m1[i])):
            tmp += (m1[i][j]-m2[i][j])**2
        sum += tmp/len(m1[i])
    mse = sum/len(m1)
    return mse


#print(MSE([[1, 2, 3], [4, 5, 6]], [[1, 1, 1], [1, 1, 1]]))
