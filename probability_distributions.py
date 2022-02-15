#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sb
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

student_avg = np.random.normal(normal_div_mean,std, size=(10_000))
student_sim = pd.DataFrame(student_avg, columns=['gpa'])
student_sim['quantiles'] = pd.qcut(student_sim['gpa'], 4, labels=False)
student_sim.quantiles.value_counts().sort_index()
ax = student_sim.plot.scatter(x='quantiles', y='gpa', rot=0)
student_sim
# %%
# exercise 3

# A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 
# click-throughs. How likely is it that this many people or more click through?

avg_click = .02
n_trials = 4326
avergae_vis_click = n_trials * avg_click

clicks = stats.poisson(avergae_vis_click).sf(96)
clicks
print('How likely is it that this many people or more click through?', clicks)


# %%
# exercise 4
# You are working on some statistics homework consisting of 100 questions where 
# all of the answers are a probability rounded to the hundreths place. Looking to 
# save time, you put down random probabilities as the answer to each question.
# What is the probability that at least one of your first 60 answers is correct?

number_correct = .01
n_sim = nrows1 = 10_000
n_test = ncol1 = 60

sim_test = (np.random.choice([0,1], (n_sim, n_test), p = [0.99, 0.01]))
prob_60 = pd.DataFrame(sim_test).round()
test_60 = prob_60 > number_correct
ds_odds = (test_60.sum(axis=1)>0).mean()
ds_odds

print('What is the probability that at least one of your first 60 answers is correct?', ds_odds)

sim_test1 = stats.binom(n_test, number_correct).sf(0)
sim_test1
print('Predicted: What is the probability that at least one of your first 60 answers is correct?', sim_test1)
# %%
# exercise 5
# The codeup staff tends to get upset when the student break area is 
# not cleaned up. Suppose that there's a 3% chance that any one student 
# cleans the break area when they visit it, and, on any given day, about 
# 90% of the 3 active cohorts of 22 students visit the break area. 
# How likely is it that the break area gets cleaned up each day? 
# How likely is it that it goes two days without getting cleaned up? 
# All week?

probability = .03
total_students = n_cols = round((3 * 22)*.90)
sim = n_rows = 10_000

clean = stats.binom(total_students, probability).sf(0)
print('How likely is it that the break area gets cleaned up each day?', clean)

clean_without_two_days = stats.binom(total_students*2, probability).pmf(0)
print('How likely is it that it goes two days without getting cleaned up?', clean_without_two_days)

clean_without_five_days = stats.binom((total_students *5), probability).pmf(0)
print('All week?', clean_without_five_days)

student_sim = (np.random.choice([0,1], (n_rows, n_cols), p = [0.97, 0.03])).reshape(n_rows,n_cols)
prob_student = pd.DataFrame(student_sim)
prob_clean = prob_student > probability
cleaned = (prob_clean.sum(axis=1)>0).mean()
cleaned
# %%
