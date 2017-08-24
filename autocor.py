import sys
import numpy as np
from glob import glob


def AR1(nbin, n, alpha):
    """
    generate nbin bins of AR(1) data with mu = 0, sigma^2 = 1

    example:
    plt.plot(AR1(3, 1000, 0.99).T)
    """
    eps = np.random.randn(nbin, n - 1) * np.sqrt(1.0 - alpha*alpha)
    x = np.empty((nbin, n))
    x[:, 0] = np.random.randn(nbin)
    for i in range(n-1):
        x[:, i+1] = alpha * x[:, i] + eps[:, i]
    return x


def sample_acf(x, max_k):
    """
    sample autocorrelation function up to lag k.
    if multiple bins, returns average over bins

    example:
    x = AR1(10, 10000, 0.9)
    plt.stem(sample_acf(x, 100), linefmt='b', markerfmt=' ', basefmt='k')
    """
    if x.ndim == 1:
        x = x.reshape(1, -1)

    nbin, n = x.shape
    x0 = x - np.mean(x, 1).reshape(-1, 1)
    gamma = np.empty(max_k)
    for k in range(max_k):
        gamma[k] = np.sum(x0[:, k:] * x0[:, :n-k])
    gamma /= gamma[0]
    return gamma


def gcm(x):
    """
    returns greatest convex minorant of some array x
    i.e. http://shabal.in/visuals/GreatestConvexMinorant.gif

    example:
    x = np.random.randn(100)
    plt.plot(np.arange(len(x)), x, np.arange(len(x)), gcm(x))
    """
    def lin(x, x1, x2, y1, y2):  # linear inter/extrapolation with two points
        return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

    n = x.shape[0]
    if n <= 2:
        return x.copy()
    nodes = [(0, x[0]), (1, x[1])]
    for i in range(2, n):
        while lin(i, nodes[-2][0], nodes[-1][0], nodes[-2][1], nodes[-1][1]) >= x[i]:
            nodes.pop()
            if len(nodes) < 2:
                break
        nodes.append((i, x[i]))

    b = np.empty_like(x)
    for (i_lo, a_i_lo), (i_hi, a_i_hi) in zip(nodes[:-1], nodes[1:]):
        for i in range(i_lo, i_hi):
            b[i] = lin(i, i_lo, i_hi, a_i_lo, a_i_hi)
    b[i_hi] = a_i_hi
    return b


def autocorr_length(x):
    """
    x has nbin bins of data with n samples each.

    calculated using initial convex sequence method on the sample acf, averaged
    over all bins.

    see http://www.mcmchandbook.net/HandbookChapter1.pdf

    example:
    alpha = 0.9993
    x = AR1(100, 10000, alpha)
    print("expected:", (1.0+alpha)/(1.0-alpha))
    print("estimated:", autocorr_length(x))
    """
    if x.ndim == 1:
        x = x.reshape(1, -1)

    nbin, n = x.shape
    x0 = x - np.mean(x, 1).reshape(-1, 1)

    # everything below is equivalent to adding together each bin's sample acf
    g0 = np.sum(x0 * x0)
    Gamma = [g0 + np.sum(x0[:, 1:] * x0[:, :n-1])]
    i = 2
    while Gamma[-1] > 0.0:
        Gamma.append(np.sum(x0[:, i:] * x0[:, :n-i]) +
                     np.sum(x0[:, i+1:] * x0[:, :n-(i+1)]))
        i += 2
    Gamma[-1] = 0.0
    Gamma = np.array(Gamma)
    Gamma /= g0

    return 2.0 * np.sum(gcm(Gamma)) - 1.0


def read_X(path, observable="X0", no=1):
    f_X_iter = sorted(glob(path + "/*_iteration_" + observable + ".dat"))
    nbin = len(f_X_iter)
    if nbin == 0:
        return

    X_iter = []
    for i, f in enumerate(f_X_iter):
        X_iter.append(np.fromfile(f))
    X_iter = np.array(X_iter)

    print("number of bins:", nbin)
    print("number of measurements per bin:", X_iter.shape[1])
    ac_len = autocorr_length(X_iter)
    print("estimate for autocorrelation length:", ac_len)
#    plt.plot(X_iter[0, :])


#def main(argv):
#    for path in argv[2:]:
#        print(path)
#        read_X(path)

if __name__ == "__main__":
    main(sys.argv)
