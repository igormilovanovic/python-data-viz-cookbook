# coding: utf-8
import random
import matplotlib
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000

# histogram buckets
buckets = 100

plt.figure()

# we need to update font size just for this example
matplotlib.rcParams.update({'font.size': 7})

plt.subplot(621)
plt.xlabel("random.random")
# Return the next random floating point number in the range [0.0, 1.0).
res = []
for _ in xrange(1, SAMPLE_SIZE):
        res.append(random.random())
plt.hist(res, buckets)

plt.subplot(622)
plt.xlabel("random.uniform")
# Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
# The end-point value b may or may not be included in the range depending on floating-point rounding in the equation a + (b-a) * random().
a = 1 
b = SAMPLE_SIZE
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.uniform(a, b))
plt.hist(res, buckets)

plt.subplot(623)
plt.xlabel("random.triangular")
# Return a random floating point number N such that low <= N <= high and with the specified mode between those bounds. The low and high bounds default to zero and one. The mode argument defaults to the midpoint between the bounds, giving a symmetric distribution.
low = 1
high = SAMPLE_SIZE
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.triangular(low, high))
plt.hist(res, buckets)

plt.subplot(624)
plt.xlabel("random.betavariate")
# Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.
alpha = 1
beta = 10
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.betavariate(alpha, beta))
plt.hist(res, buckets)

plt.subplot(625)
plt.xlabel("random.expovariate")
# Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero. (The parameter would be called “lambda”, but that is a reserved word in Python.) Returned values range from 0 to positive infinity if lambd is positive, and from negative infinity to 0 if lambd is negative.
lambd = 1.0 / ((SAMPLE_SIZE + 1) / 2.)
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.expovariate(lambd))
    
plt.hist(res, buckets)

plt.subplot(626)
plt.xlabel("random.gammavariate")
# Gamma distribution. (Not the gamma function!) Conditions on the parameters are alpha > 0 and beta > 0.
# The probability distribution function is:
#
#           x ** (alpha - 1) * math.exp(-x / beta)
# pdf(x) =  --------------------------------------
#             math.gamma(alpha) * beta ** alpha
alpha = 1
beta = 10
res = []
for _ in xrange(1, SAMPLE_SIZE):
        res.append(random.gammavariate(alpha, beta))
plt.hist(res, buckets)

plt.subplot(627)
plt.xlabel("random.lognormvariate")
# Log normal distribution. If you take the natural logarithm of this distribution, you’ll get a normal distribution with mean mu and standard deviation sigma. mu can have any value, and sigma must be greater than zero.
mu = 1
sigma = 0.5
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.lognormvariate(mu, sigma))
plt.hist(res, buckets)

plt.subplot(628)
plt.xlabel("random.normalvariate")
# Normal distribution. mu is the mean, and sigma is the standard deviation.
mu = 1
sigma = 0.5
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.normalvariate(mu, sigma))
plt.hist(res, buckets)

plt.subplot(629)
plt.xlabel("random.paretovariate")
# Pareto distribution. alpha is the shape parameter.
alpha = 1
res = []
for _ in xrange(1, SAMPLE_SIZE):
    res.append(random.paretovariate(alpha))
plt.hist(res, buckets)

plt.tight_layout()
plt.show()
