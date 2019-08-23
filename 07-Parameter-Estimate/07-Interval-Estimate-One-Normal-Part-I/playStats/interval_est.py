from playStats.descriptive_stats import mean, std, variance
from math import sqrt
from scipy.stats import norm, t, chi2


def mean_ci_est(data, alpha, sigma=None):

    n = len(data)
    sample_mean = mean(data)

    if sigma is None:
        # 方差未知
        s = std(data)
        se = s/sqrt(n)
        t_value = abs(t.ppf(alpha/2, n-1))
        return sample_mean - se * t_value, sample_mean + se * t_value

    else:
        # 方差已知
        se = sigma/sqrt(n)
        z_value = abs(norm.ppf(alpha / 2))
        return sample_mean - se * z_value, sample_mean + se * z_value