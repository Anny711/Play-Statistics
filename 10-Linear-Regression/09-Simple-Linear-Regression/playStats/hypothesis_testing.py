from math import sqrt
from playStats.descriptive_stats import mean, std, variance, cor, covariance
from scipy.stats import norm, t, chi2, f

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


def t_test(data1, data2=None, tail="both", mu=0, equal=True):

    assert tail in ["both", "left", "right"], \
        'tail should be one of "both", "left", "right"'

    if data2 is None:
        mean_val = mean(data1)
        se = std(data1) / sqrt(len(data1))
        t_val = (mean_val - mu) / se
        df = len(data1) - 1
    else:
        n1 = len(data1)
        n2 = len(data2)
        mean_diff = mean(data1) - mean(data2)
        sample1_var = variance(data1)
        sample2_var = variance(data2)

        if equal:
            sw = sqrt(((n1 - 1) * sample1_var + (n2 - 1) * sample2_var) / (n1 + n2 - 2))
            t_val = (mean_diff - mu) / (sw * sqrt(1/n1 + 1/n2))
            df = n1 + n2 - 2
        else:
            se = sqrt(sample1_var/n1 + sample2_var/n2)
            t_val = (mean_diff - mu) / se
            df_numerator = (sample1_var / n1 + sample2_var / n2) ** 2
            df_denominator = (sample1_var / n1) ** 2 / (n1 - 1) + (sample2_var / n2) ** 2 / (n2 - 1)
            df = df_numerator / df_denominator

    if tail == "both":
        p = 2 * (1 - t.cdf(abs(t_val), df))
    elif tail == "left":
        p = t.cdf(t_val, df)
    else:
        p = 1 - t.cdf(t_val, df)

    return t_val, df, p


def t_test_paired(data1, data2, tail="both", mu=0):
    data = [e1 - e2 for (e1, e2) in zip(data1, data2)]
    return t_test(data, tail=tail, mu=mu)


def chi2_test(data, tail="both", sigma2=1):

    assert tail in ["both", "left", "right"], \
        'tail should be one of “both”, “left”, “right”'

    n = len(data)
    sample_var = variance(data)
    chi2_val = (n - 1)*sample_var/sigma2

    if tail == "both":
        p = 2 * min(1 - chi2.cdf(chi2_val, n-1), chi2.cdf(chi2_val, n-1))
    elif tail == "left":
        p = chi2.cdf(chi2_val, n-1)
    else:
        p = 1 - chi2.cdf(chi2_val, n-1)

    return chi2_val, n-1, p


def f_test(data1, data2, tail="both", ratio=1):

    assert tail in ["both", "left", "right"], \
        'tail should be one of “both”, “left”, “right”'

    n1 = len(data1)
    n2 = len(data2)
    sample1_var = variance(data1)
    sample2_var = variance(data2)
    f_val = sample1_var/sample2_var/ratio
    df1 = n1 - 1
    df2 = n2 - 1

    if tail == "both":
        p = 2 * min(1 - f.cdf(f_val, df1, df2), f.cdf(f_val, df1, df2))
    elif tail == "left":
        p = f.cdf(f_val, df1, df2)
    else:
        p = 1 - f.cdf(f_val, df1, df2)

    return f_val, df1, df2, p


def anova_oneway(data):

    k = len(data)
    assert k > 1

    group_means = [mean(group) for group in data]
    group_szs = [len(group) for group in data]
    n = sum(group_szs)
    assert n > k

    grand_mean = sum(group_mean * group_sz for group_mean, group_sz in zip(group_means, group_szs))/n

    sst = sum(sum((y - grand_mean) ** 2 for y in group) for group in data)
    ssg = sum((group_mean - grand_mean)**2*group_sz for group_mean, group_sz in zip(group_means, group_szs))
    sse = sst - ssg

    dfg = k - 1
    dfe = n - k

    msg = ssg/dfg
    mse = sse/dfe

    f_value = msg/mse
    p = 1 - f.cdf(f_value, dfg, dfe)

    return f_value, dfg, dfe, p


def cor_test(data1, data2):

    r = cor(data1, data2)
    if r**2 == 1:
        return r, None, None, None

    n = len(data1)
    assert n > 2

    t_value = r/sqrt((1 - r**2)/(n-2))
    p = 2 * (1 - t.cdf(abs(t_value), n-2))

    return r, t_value, n-2, p


def simple_linear_reg(y, x):

    assert len(x) == len(y)

    n = len(x)
    assert n > 1

    mean_x = mean(x)
    mean_y = mean(y)

    beta1 = covariance(x, y) / variance(x)
    beta0 = mean_y - beta1 * mean_x

    y_hat = [beta0 + beta1 * e for e in x]
    ss_residual = sum((e1 - e2)**2 for e1, e2 in zip(y, y_hat))
    se_model = sqrt(ss_residual / (n-2))

    t_value = beta1 / (se_model / sqrt((n-1)*variance(x)))
    p = 2 * (1 - t.cdf(abs(t_value), n - 2))

    return beta0, beta1, t_value, n - 2, p

























