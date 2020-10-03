import numpy as np
from scipy.signal import hilbert


def dsbsc(mt, ct):
    return mt*ct


def conv(mt, ct):
    mnt = mt/max(abs(mt))
    a = float(input("enter modulation index a (0<a<1) :"))
    ut = ct*(1+a*mnt)
    return ut


def ssb(mt, ct):
    mc = hilbert(mt)
    ut = 0.5*(ct*mt - ct*mc)
    return ut


# def vsb(mt, ct):
