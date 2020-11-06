from general import *
import matplotlib.pyplot as plt
from AM import dsbsc
import numpy as np


def FDM(msgfq, carfc, mod_tech):
    tpm = 1/min(carfc)
    tm = np.arange(0, 10*tpm, tpm/1000)
    mt, ct = [], []
    for i in range(len(msgfq)):
        mt.append(np.cos(2*np.pi*msgfq[i]*tm))
        ct.append(np.cos(2*np.pi*carfc[i]*tm))
    ut = []
    multmsg = [0]*tm
    for i in range(len(mt)):
        mod_tmp = mod_tech(mt[i], ct[i])
        multmsg += mod_tmp
        ut.append(mod_tmp)
    plt.figure(figsize=(10, 10))
    for i in range(4):
        cplot(plt.subplot2grid((4, 5), (i, 0)), tm, mt[i], '', '', '')
        cplot(plt.subplot2grid((4, 5), (i, 1)), tm, ct[i], '', '', '')
        cplot(plt.subplot2grid((4, 5), (i, 2)), tm, ut[i], '', '', '')
    cplot(plt.subplot2grid((4, 5), (1, 3), colspan=2,
                           rowspan=2), tm, multmsg, '', '', '')
    plt.tight_layout()
    plt.show()
    return multmsg, msgfq, carfc, mod_tech


print(FDM([100, 200, 300, 400], [5000, 6000, 7000, 8000], dsbsc))
