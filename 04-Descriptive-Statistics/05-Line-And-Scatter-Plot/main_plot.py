import matplotlib.pyplot as plt
import random

if __name__ == "__main__":

    # scatter plot
    random.seed(666)
    x = [random.randint(0,100) for _ in range(100)]
    y = [random.randint(0,100) for _ in range(100)]
    plt.scatter(x, y)
    plt.show()

    # line plot
    x = [random.randint(0, 100) for _ in range(100)]
    plt.plot([i for i in range(100)], x)
    plt.show()