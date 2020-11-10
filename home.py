import numpy as np
import matplotlib.pyplot as plt
import AM
import DM
from compare import comp
from scipy.fftpack import fft, fftfreq
from general import cplot
"""
Input
fm = frequency of message signal'
fc = frequency of carrier signal
tpc/tpm = time period of carrier/message
"""
fm = float(input('Enter message signal frequency: '))
fc = float(input('Enter carrier wave frequency: '))
tpm = 1/(fm)
tpc = 1/(fc)
fs = 100/tpc
tm = np.arange(0, 10*tpm, tpc/100)
tc = np.arange(0, 10*tpm, tpc/100)
mt = np.sin(2*np.pi*fm*tm)
ct = np.cos(2*np.pi*fc*tc)
"""
selection of the Amplitude modulation techniques
"""
ch = input(
    '1) DSBSC AM \n2)CONVENIONAL AM \n3)SSB\n4)VSB \n5)compare all outputs\nyour choice: ')
tech = {'1': [AM.dsbsc, DM.dmdsbsc], '2': [
    AM.conv], '3': [AM.ssb, DM.dmssb], '5': comp}

try:
    modulator, demodulator = tech[ch]
    ut = modulator(mt, ct, fc, tm)
    dm_sig = demodulator(ut, fc, fs, tm)
    #uf = fft(ut)
    #fax = fftfreq(len(uf))*tpc
except:
    tech[ch](mt, ct, tm, tc)
"""
ploting input and output signal
"""
ax1 = plt.subplot2grid((3, 2), (0, 0))
ax2 = plt.subplot2grid((3, 2), (0, 1))
ax3 = plt.subplot2grid((3, 2), (1, 0), colspan=2)
ax4 = plt.subplot2grid((3, 2), (2, 0), colspan=2)
cplot(ax1, tm, mt, 't', 'm(t)', 'message signal')
cplot(ax2, tm, ct, 't', 'c(t)', 'carrier signal')
cplot(ax3, tm, ut, 't', 'u(t)', 'modulated signal')
cplot(ax4, tm, dm_sig, 'f', 'm(t)', 'demodulated signal')
plt.tight_layout()
plt.show()
