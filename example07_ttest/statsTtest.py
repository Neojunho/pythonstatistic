import numpy as np

# from scipy import stats
import scipy.stats as stats
np.random.seed(12345678)

rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
print(rvs1)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=500)
print(stats.ttest_ind(rvs1,rvs2))

stats.ttest_ind(rvs1,rvs2, equal_var = False)