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


def var_ci_est(data, alpha):

    n = len(data)
    s2 = variance(data)
    chi2_lower_value = chi2.ppf(alpha/2, n-1)
    chi2_upper_value = chi2.ppf(1-alpha/2, n-1)
    return (n-1) * s2 / chi2_upper_value, (n-1) * s2 / chi2_lower_value


def mean_diff_ci_t_est(data1, data2, alpha, equal=True):

    n1 = len(data1)
    n2 = len(data2)
    mean_diff = mean(data1) - mean(data2)

    sample1_var = variance(data1)
    sample2_var = variance(data2)

    if equal:
        sw = sqrt(((n1-1)*sample1_var + (n2-1)*sample2_var)/(n1 + n2 - 2))
        t_value = abs(t.ppf(alpha/2, n1+n2-2))
        return mean_diff - sw*sqrt(1/n1 + 1/n2)*t_value, \
               mean_diff + sw*sqrt(1/n1 + 1/n2)*t_value

    else:
        df_numerator = (sample1_var/n1 + sample2_var/n2)**2
        df_denominator = (sample1_var/n1)**2/(n1-1) + (sample2_var/n2)**2/(n2-1)
        df = df_numerator / df_denominator
        t_value = abs(t.ppf(alpha/2, df))
        return mean_diff - sqrt(sample1_var/n1 + sample2_var/n2)*t_value, \
               mean_diff + sqrt(sample1_var/n1 + sample2_var/n2)*t_value









