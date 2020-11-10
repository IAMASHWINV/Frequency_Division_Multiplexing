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
