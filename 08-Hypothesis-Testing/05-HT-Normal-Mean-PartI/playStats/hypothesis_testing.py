from math import sqrt
from playStats.descriptive_stats import mean
from scipy.stats import norm

def z_test(data1, data2=None, tail="both", mu=0, sigma1=1, sigma2=None):

    assert tail in ["both", "left", "right"], \
           'tail should be one of "both", "left", "right"'

    if data2 is None:
        mean_val = mean(data1)
        se = sigma1 / sqrt(len(data1))
        z_val = (mean_val - mu) / se
    else:
        assert sigma2 is not None
        mean_diff = mean(data1) - mean(data2)
        se = sqrt(sigma1**2 / len(data1) + sigma2**2 / len(data2))
        z_val = (mean_diff - mu) / se

    if tail == "both":
        p = 2*(1 - norm.cdf(abs(z_val)))
    elif tail == "left":
        p = norm.cdf(z_val)
    else:
        p = 1 - norm.cdf(z_val)

    return z_val, p