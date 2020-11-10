import numpy as np
from scipy.signal import hilbert


def dsbsc(mt, ct, fc, tm):
    return mt*ct


def conv(mt, ct, fc, tm):
    mnt = mt/max(abs(mt))
    a = float(input("enter modulation index a (0<a<1) :"))
    ut = ct*(1+a*mnt)
    return ut


def ssb(mt, ct, fc, tm):
    mc = hilbert(mt)
    c1 = np.cos(2*np.pi*fc*tm)
    c2 = np.sin(2*np.pi*fc*tm)
    ut = 0.5*(c1*mt - c2*mc)
    return list(map(float, ut))


# def vsb(mt, ct):
