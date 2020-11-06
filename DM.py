import numpy as np
from general import butter_lowpass_filter
import matplotlib.pyplot as plt
from AM import conv


def dmdsbsc(ut, fc, fs, t):
    vt = ut*np.cos(2*np.pi*fc*t + np.pi/4)
    mt = butter_lowpass_filter(vt, fc/2, fs, 4)
    return (mt)*2/np.cos(np.pi/4)


'''
fm = float(0.04)
fc = float(0.5)
tpm = 1/(fm)
tpc = 1/(fc)
fs = 100/tpc
tm = np.arange(0, 10*tpm, tpc/100)
tc = np.arange(0, 10*tpm, tpc/100)
mt = np.sin(2*np.pi*fm*tm)
ct = np.cos(2*np.pi*fc*tc)
plt.subplot(3, 1, 1)
plt.plot(tm, mt)
ut = conv(mt, ct)
plt.subplot(3, 1, 2)
plt.plot(tm, ut)
rect = butter_lowpass_filter(ut, fm, fs, 2)
plt.subplot(3, 1, 3)
plt.plot(tm, rect)
plt.show()
'''
