from collections import Counter
from playStats.descriptive_stats import frequency

if __name__ == "__main__":

    # 测试频数
    data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    counter = Counter(data)
    print(counter.most_common())
    print(counter.most_common()[0][1])

    # 测试频率
    freq = frequency(data)
    print(freq)