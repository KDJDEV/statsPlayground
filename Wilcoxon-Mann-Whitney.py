from scipy.stats import mannwhitneyu
import numpy as np

data1 = [1, 1, 1, 1, 1, 1, 5, 6, 6, 6, 6, 6, 6]
data2 = [4, 4, 4, 4, 4, 4, 5, 9, 9, 9, 9, 9, 9]

statistic, p_value = mannwhitneyu(data1, data2, alternative='two-sided')

print(f'Mann-Whitney U statistic: {statistic}')
print(f'p-value: {p_value}')

#what this first example shows it that the Mann-Whitney U test only tells you that the distributions look different, without the further assumption that they have similar shapes. Only with that assumption can you conclude difference in medians.

np.random.seed(0) 

groupA = np.random.normal(loc=0, scale=1, size=100)

groupB = np.random.normal(loc=0, scale=10000, size=100)

statistic, p_value = mannwhitneyu(groupA, groupB, alternative='two-sided')

print(f'Mann-Whitney U statistic: {statistic:.2f}')
print(f'p-value: {p_value:.4f}')

print(f'Median of group A: {np.median(groupA):.2f}')
print(f'Median of group B: {np.median(groupB):.2f}')