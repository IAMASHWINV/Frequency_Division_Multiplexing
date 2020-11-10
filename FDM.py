from general import *
import matplotlib.pyplot as plt
from AM import dsbsc, ssb
from DM import dmdsbsc, dmssb
import numpy as np


def FDM(msgfq, carfc, mod_tech):
    tpm = 1/(3*max(carfc))
    tmax = 1/min(msgfq)
    tm = np.arange(0, tmax, tpm)
    mt, ct = [], []
    for i in range(len(msgfq)):
        mt.append(np.cos(2*np.pi*msgfq[i]*tm))
        ct.append(np.cos(2*np.pi*carfc[i]*tm))
    ut = []
    multmsg = [0]*tm
    for i in range(len(mt)):
        mod_tmp = mod_tech[0](mt[i], ct[i], carfc[i], tm)
        multmsg += mod_tmp
        ut.append(mod_tmp)
    plt.figure(figsize=(10, 10))
    for i in range(4):
        cplot(plt.subplot2grid((4, 5), (i, 0)), tm, mt[i], '', '', '')
        cplot(plt.subplot2grid((4, 5), (i, 1)),
              tm[:50], ct[i][:50], '', '', '')
        cplot(plt.subplot2grid((4, 5), (i, 2)), tm, ut[i], '', '', '')
    cplot(plt.subplot2grid((4, 5), (1, 3), colspan=2,
                           rowspan=2), tm, multmsg, '', '', '')
    plt.tight_layout()
    RetFDM(multmsg, msgfq, carfc, mod_tech[1], tm)
    plt.show()


def RetFDM(multmsg, msgfq, carfc, mod_tech, tm):
    fs = 3*max(carfc)
    plt.figure(2, figsize=(10, 10))
    cplot(plt.subplot2grid((4, 5), (1, 0), colspan=2,
                           rowspan=2), tm, multmsg, '', '', '')
    bpf = []
    obt_sig = []
    for i in range(len(msgfq)):
        bpf_tmp = butter_bandpass_filter(
            multmsg, [0.95*(carfc[i]-msgfq[i]), 1.2*(carfc[i]+msgfq[i])], fs, 4)
        obt_temp = mod_tech(bpf_tmp, carfc[i], fs, tm)
        obt_sig.append(obt_temp)
        bpf.append(bpf_tmp)
    for i in range(4):
        cplot(plt.subplot2grid((4, 5), (i, 2)), tm, bpf[i], '', '', '')
        cplot(plt.subplot2grid((4, 5), (i, 3), colspan=2),
              tm, obt_sig[i], '', '', '')
        # cplot(plt.subplot2grid((4, 5), (i, 4)), tm, ut[i], '', '', '')
    plt.tight_layout()


print(FDM([1, 2, 3, 4], [1000, 2000, 3000, 4000], [ssb, dmssb]))
