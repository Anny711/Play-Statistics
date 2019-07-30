from collections import Counter

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



















