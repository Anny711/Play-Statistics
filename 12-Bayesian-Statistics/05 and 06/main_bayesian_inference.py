from scipy.stats import binom
import matplotlib.pyplot as plt
import random


if __name__ == "__main__":

    # data
    nResponders = 78
    nTested = 100

    # setting up hypotheses/models
    parameters = [x / 100 for x in range(1, 100)]

    # specifying prior probability
    priors = [1 / len(parameters)] * len(parameters)

    # # plot prior probability
    #     # plt.plot(parameters, priors)
    #     # plt.show()

    # calculate likelihood
    likelihoods = [binom.pmf(nResponders, nTested, parameter) for parameter in parameters]

    # # plot likelihoods
    # plt.plot(parameters, likelihoods)
    # plt.show()

    # calculate marginal_likelihood
    marginal_likelihood = sum([likelihood * prior for likelihood, prior in zip(likelihoods, priors)])

    # calculate posterior
    posteriors = [(likelihood * prior) / marginal_likelihood for likelihood, prior in zip(likelihoods, priors)]

    # # plot posterior probability
    # plt.plot(parameters, posteriors)
    # plt.show()

    # find the parameter with the highest posterior probability
    ind = posteriors.index(max(posteriors))
    print(parameters[ind])

    # compute credible intervals
    n = 100000 # number of iterations
    # create random uniform variates for x and y
    x = [random.uniform(0.0, 1.0) for _ in range(n)]  # parameter
    y = [random.uniform(0.0, 1.0) for _ in range(n)]  # posterior probability of the parameter
    # calculate f(x), the actual posterior probability
    fx = [binom.pmf(nResponders, nTested, parameter) for parameter in x]
    # accept samples where y < f(x)
    accept_x = [x[i] for i in range(0, len(x)) if y[i] < fx[i]]
    accept_x = sorted(accept_x)

    # plot distribution of accepted x values
    plt.hist(accept_x, bins=100)
    plt.show()

    # find a 95% credible interval
    print(accept_x[int(0.025 * len(accept_x))],
          accept_x[int(0.975 * len(accept_x))])
