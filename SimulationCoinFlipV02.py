import numpy as np
from scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt

#Input
n_flip = 3
result_1set = list(range(n_flip))
prob_HT = 0.50
n_sim = 5000
result_list = []

#Begin binomial distribution (beacuse it discretely will return 0 or 1)
print("I set coin probability =", prob_HT)
print("My sign convention are: Tails = 0, Heads = 1")
for iter in range(0, n_sim):
    result_1set = binom.rvs(1, prob_HT, size=n_flip)
    result_list.append(result_1set)

result_a = np.asarray(result_list)
print(result_list)
print("Head Count: ", np.count_nonzero(result_a == 1))
print("Tail Count: ", np.count_nonzero(result_a == 0))
df = pd.DataFrame(data = result_a)
df.to_csv('results_kkavee.csv', index=False,header=False)

#Visualise
df["Total"] = df.sum(axis=1)
data_to_plot = df["Total"].to_numpy()

plt.hist(data_to_plot)
plt.title("Histogram of Head")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig('histogram_kkavee.png')
#plt.show()