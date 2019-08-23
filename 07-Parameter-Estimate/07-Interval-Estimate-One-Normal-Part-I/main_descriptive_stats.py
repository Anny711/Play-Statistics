from collections import Counter
from playStats.descriptive_stats import frequency
from playStats.descriptive_stats import mode
from playStats.descriptive_stats import median
from playStats.descriptive_stats import mean
from playStats.descriptive_stats import rng
from playStats.descriptive_stats import quartile
from playStats.descriptive_stats import variance
from playStats.descriptive_stats import std

if __name__ == "__main__":

    # # 测试频数
    # data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    # counter = Counter(data)
    # print(counter.most_common())
    # print(counter.most_common()[0][1])
    #
    # # 测试频率
    # freq = frequency(data)
    # print(freq)

    # # 测试众数
    # # data = [2, 2, 2, 1, 1, 1, 3, 3]
    # data = [2, 1, 3]
    # mode_elements, mode_count = mode(data)
    # print(mode_elements)
    # print(mode_count)
    #
    # if mode_elements:
    #     print(mode_elements)
    #     print(mode_count)
    # else:
    #     print("Mode does not exist.")

    # # 测试中位数
    # data = [1, 4, 2, 3]
    # print(median(data))
    #
    # data = [1, 4, 2, 3, 5]
    # print(median(data))
    #
    # data = [1, 4, 2, 3, 5, 99]
    # print(median(data))

    # # 测试均值
    # data = [1, 4, 2, 3, 5, 99]
    # print(mean(data))

    # # 测试极差
    # data = [1, 4, 2, 3, 5, 99]
    # print(rng(data))

    # # 测试四分位数
    # data = [1, 4, 2, 3, 5, 8]
    # print(quartile(data))

    # 测试方差
    data = [1, 4, 2, 3, 5, 8]
    print(variance(data))

    # 测试标准差
    print(std(data))





