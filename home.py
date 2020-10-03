import numpy as np
import matplotlib.pyplot as plt
import AM
import compare
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
tm = np.arange(0, 2*tpm, tpc/100)
tc = np.arange(0, 2*tpm, tpc/100)
mt = np.sin(2*np.pi*fm*tm)
ct = np.cos(2*np.pi*fc*tc)
"""
selection of the Amplitude modulation techniques
"""
ch = input('1) DSBSC AM \n2)CONVENIONAL AM \n3)SSB \n5)compare all outputs')
tech = {'1': AM.dsbsc, '2': AM.conv, '3': AM.ssb, '5': compare.comp}
try:
    ut = tech[ch](mt, ct)
except:
    tech[ch](mt, ct, tm, tc)
"""
ploting input and output signal
"""
fig, axes = plt.subplots(nrows=3, ncols=2)
axes[0, 0].plot(tm, mt)
axes[0, 0].set_title('message signal')
axes[0, 0].set_xlabel('time')
axes[0, 0].set_ylabel('m(t)')
axes[0, 0].grid(True)
axes[0, 1].plot(tc, ct)
axes[0, 1].set_title('carrier signal')
axes[0, 1].set_xlabel('time')
axes[0, 1].set_ylabel('c(t)')
axes[0, 1].grid(True)
"""
ploting amplitude modulated signal
"""
gs = axes[1, 1].get_gridspec()
for ax in axes[1, :]:
    ax.remove()

axam = fig.add_subplot(gs[1, :])
axam.plot(tc, ut)
axam.set_title('modulated signal')
axam.set_xlabel('time')
axam.set_ylabel('u(t)')
axam.grid(True)

axes[2, 1].plot(tc, ut)
axes[2, 1].set_title('modulated signal')
axes[2, 1].set_xlabel('time')
axes[2, 1].set_ylabel('u(t)')
axes[2, 1].grid(True)
fig.tight_layout()
plt.show()
