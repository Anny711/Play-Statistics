from collections import Counter
from math import sqrt

def frequency(data):
    """频率"""
    counter = Counter(data)
    ret = []
    for point in counter.most_common():
        ret.append((point[0], point[1] / len(data)))
    return ret


def mode(data):
    """众数"""
    counter = Counter(data)
    if counter.most_common()[0][1] == 1:
        return None, None

    count = counter.most_common()[0][1]
    ret = []
    for point in counter.most_common():
        if point[1] == count:
            ret.append(point[0])
        else:
            break
    return ret, count


def median(data):
    """中位数"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]

    return (sorted_data[n // 2 -1] + sorted_data[n // 2]) / 2


def mean(data):
    """均值"""
    return sum(data) / len(data)


def rng(data):
    """极差"""
    return max(data) - min(data)


def quartile(data):
    """四分位数"""
    n = len(data)
    q1, q2, q3 = None, None, None
    if n >= 4:
        sorted_data = sorted(data)
        q2 = median(sorted_data)
        if n % 2 == 1:
            """
            `sorted_data[n // 2 + 1:]` 表示从索引 `n // 2 + 1` 开始到数据集末尾的子集。

            让我们解释一下这个表达式的不同部分：
            - `n // 2` 表示整数除法运算，得到 `n` 的一半。如果 `n` 是奇数，这将返回小于 `n` 的最大整数，如果 `n` 是偶数，这将返回 `n` 的一半。
            - `+ 1` 表示在 `n // 2` 的基础上再加 1，即下一个索引位置。
            - `sorted_data[n // 2 + 1:]` 表示从索引 `n // 2 + 1` 开始到数据集末尾的子集，包括索引 `n // 2 + 1` 的元素。

            冒号表示一个切片操作（slicing operation），用于从一个可迭代对象（例如列表、字符串等）中选择一部分元素。
            切片操作的一般形式是 `start:end:step`，其中 `start` 表示起始位置（默认为 0），`end` 表示结束位置（但不包括该位置的元素），`step` 表示步长（默认为 1）。
            """
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2 + 1:])
        else:
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2:])

    return q1, q2, q3


def variance(data):
    """方差"""
    n = len(data)
    if n <= 1:
        return None

    mean_value = mean(data)
    return sum((e - mean_value) ** 2 for e in data) / (n - 1)


def std(data):
    """标准差"""
    return sqrt(variance(data))





















