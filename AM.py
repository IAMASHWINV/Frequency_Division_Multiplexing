import numpy as np
from scipy.signal import hilbert
from scipy import fft


def dsbsc(mt, ct, fc, tm):
    return mt*ct


def conv(mt, ct, fc, tm, a=1):
    mnt = (mt)/max(abs(mt))
    ut = (1+a*mnt)*np.cos(2*np.pi*fc*tm)
    return ut


def ssb(mt, ct, fc, tm):
    mc = hilbert(mt)
    c1 = np.cos(2*np.pi*fc*tm)
    c2 = np.sin(2*np.pi*fc*tm)
    ut = 0.5*(c1*mt - c2*mc)
    return list(map(float, ut))
