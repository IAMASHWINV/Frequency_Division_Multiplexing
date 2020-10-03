def cplot(ax, t, s, xl, yl, tit):
    ax.plot(t, s)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.set_title(tit)
    ax.grid(True)
