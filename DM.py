import numpy as np
from general import butter_lowpass_filter
import matplotlib.pyplot as plt
from AM import ssb

# demodulation dsbsc


def dmdsbsc(ut, fc, fs, t):
    vt = ut*np.cos(2*np.pi*fc*t + np.pi/4)
    mt = butter_lowpass_filter(vt, fc/2, fs, 4)
    return (mt)*2/np.cos(np.pi/4)


def dmssb(ut, fc, fs, t):
    cm = np.cos(2*np.pi*fc*t)
    pmt = ut*cm
    mt = butter_lowpass_filter(pmt, fc/2, fs, 5)
    return 4*mt


'''
fm = float(0.04)
fc = float(0.5)
tpm = 1/(fm)
tpc = 1/(fc)
fs = 100/tpc
tm = np.arange(0, 10*tpm, tpc/100)
tc = np.arange(0, 10*tpm, tpc/100)
mt = np.cos(2*np.pi*fm*tm)
ct = np.sin(2*np.pi*fc*tc)
plt.subplot(3, 1, 1)
plt.plot(tm, mt)
ut = ssb(mt, ct, fc, tm)
plt.subplot(3, 1, 2)
plt.plot(tm, ut)
rect = dmssb(ut, fc, fs, tm)
plt.subplot(3, 1, 3)
plt.plot(tm, rect)
plt.show()
'''
