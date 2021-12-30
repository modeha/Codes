import matplotlib.pyplot as plt
from scipy.stats import norm
#Produce 1000 Random Variable following normal distribution
r = norm.rvs(size=1000)
#Plotting the distribution
fig, ax = plt.subplots(1, 1)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()