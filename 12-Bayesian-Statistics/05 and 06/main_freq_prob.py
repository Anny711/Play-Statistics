import random
import matplotlib.pyplot as plt


def toss():
    return random.randint(0, 1)


if __name__ == "__main__":

    indices = []
    freq = []
    for toss_num in range(10, 10001, 10):

        heads = 0
        for _ in range(toss_num):
            if toss() == 0:
                heads += 1
        freq.append(heads / toss_num)
        indices.append(toss_num)

    plt.plot(indices, freq)
    plt.show()