#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
import viz # curriculum viz example code

np.random.seed(123)
#%%
# exercise 1
# A bank found that the average number of cars waiting during the noon 
# hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. 
# Make a chart of this distribution and answer these questions concerning the 
# probability of cars waiting at the drive-up window.
# 1a. What is the probability that no cars drive up in the noon hour?
# 1b. What is the probability that 3 or more cars come through the drive through?
# 1c. How likely is it that the drive through gets at least 1 car?

avg_cars = 2


pd.Series(stats.poisson(avg_cars).rvs(10_000)).value_counts().sort_index().plot.bar(width=1, ec='blue')
plt.title('average car in drive thru')
plt.ylabel('prob of cars (x)')
plt.show()
#%%

zero_cars = stats.poisson(avg_cars).pmf(0)
print('What is the probability that no cars drive up in the noon hour?', zero_cars)

three_or_more = stats.poisson(avg_cars).sf(3)

print('What is the probability that 3 or more cars come through the drive through?', three_or_more)

at_least_one = stats.poisson(avg_cars).sf(0)
print('How likely is it that the drive through gets at least 1 car?', at_least_one)
# %%
# exercise 2
# Grades of State University graduates are normally distributed with a mean of 
# 3.0 and a standard deviation of .3. 
# Calculate the following:
# What grade point average is required to be in the top 5% of the graduating class?
# What GPA constitutes the bottom 15% of the class?
# An eccentric alumnus left scholarship money for students in the third decile from 
# the bottom of their class. Determine the range of the third decile. Would a student 
# with a 2.8 grade point average qualify for this scholarship?
# If I have a GPA of 3.5, what percentile am I in?

std = 0.3
normal_div_mean = 3

top_five = stats.norm(normal_div_mean,std).isf(.05)
print('What grade point average is required to be in the top 5%''of the graduating class?', top_five)

bottem_fifteen = stats.norm(normal_div_mean,std).ppf(0.15)
print('What GPA constitutes the bottom 15%''of the class?', bottem_fifteen)

third_decile = stats.norm(normal_div_mean,std).cdf(3.5)
print('what is the range of the third decile', third_decile)

what_percentile = (np.random.normal(normal_div_mean,std, 10_000)< 3.5).mean()
print('If I have a GPA of 3.5, what percentile am I in?', what_percentile)

# %%
