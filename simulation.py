#%%
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
import viz

# %%
#excercise 1 
n_trials1 = nrows1 = 10_000
n_dice1 = ncols1 = 2

rolls_dice = np.random.choice([1,2,3,4,5,6], n_trials1 * n_dice1).reshape(nrows1, ncols1)
double = pd.DataFrame(rolls_dice, columns=['dice_1','dice_2'])
is_double = double.where((double['dice_1'] == double['dice_2']))
#divid is_double.count() by 10_000
prob = is_double.count() / n_trials1
print('How likely is it that you roll doubles when rolling two dice?', prob)

#%%
#excercise 2

coin_trials = nrows2 = 10_000
n_coin = ncols2 = 8
#heads=0
coin_flip = np.random.choice([0,1], coin_trials * n_coin).reshape(nrows2, ncols2)
total_flips = pd.DataFrame(coin_flip, columns=['coin_1','coin_2','coin_3','coin_4','coin_5','coin_6','coin_7','coin_8'])
sum_total_flips = total_flips.sum(axis=1)
heads = sum_total_flips ==3
heads_mean = heads.mean()
heads_mean

greater_than_three = sum_total_flips > 3
greater_than_three_mean = greater_than_three.mean()
greater_than_three_mean
print('If you flip 8 coins, what is the probability of getting exactly 3 heads?',heads_mean)
print('What is the probability of getting more than 3 heads?',greater_than_three_mean)
# %%
#Excercise 3
#There are approximitely 3 web development cohorts for every 1 data science 
#cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on 
#a billboard, what are the odds that the two billboards I drive past both have 
#data science students on them?
data_scinece = .25 
n_sim= nrows3 = 10_000 
n_cohorts = ncols3 = 2

cohorts = np.random.random((n_sim * n_cohorts)).reshape(nrows3, ncols3)
prob_data = pd.DataFrame(cohorts)
select_data = prob_data < data_scinece
ds_odds = (select_data.sum(axis=1) == 2).mean()
print('what are the odds that the two billboards I drive past both have data science students on them?', ds_odds) 

# %%
# exercise 4
# Codeup students buy, on average, 3 poptart packages with 
# a standard deviation of 1.5 a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, 
# how likely is it that I will be able to buy some poptarts on Friday
# afternoon? (Remember, if you have mean and standard deviation, use t
# he np.random.normal)

poptart_std = 1.5
poptart_avg = 3 


poptarts = np.random.normal(poptart_avg, poptart_std, size=(10_000,5)).round()
poptarts = np.where(poptarts < 0, 0, poptarts)
prob_poptart = pd.DataFrame(poptarts, columns=['monday','tuesday','wednesday','thursday','friday'])
total_poptarts = (prob_poptart.sum(axis=1) <= 16).mean()
#left_over = 17 - total_poptarts
#left_over_mean = (left_over >= 1).mean()
print('how likely is it that I will be able to buy some poptarts on Friday afternoon?', total_poptarts)

# %%
# exercise 5 
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# Since you have means and standard deviations, you can use np.random.normal 
# to generate observations.
# If a man and woman are chosen at random, P(woman taller than man)?
men_avg = 178
men_std = 6
women_avg = 170
women_std = 6

avg_hieght = np.random.normal((men_avg, men_std),(women_avg,women_std), size=(10_000,2))
prob_height = pd.DataFrame(avg_hieght, columns=['men','women'])
prob_height['are taller'] = prob_height.apply(lambda x: x['women'] if x['women'] > x['men'] else np.nan, axis=1)
women_prob = prob_height.count() / 10_000
#random_prob_height = prob_height.where((prob_height['women'] > prob_height['men']),)
#women_prob = random_prob_height.count() 

print('If a man and woman are chosen at random, P(woman taller than man), =',women_prob)


# %%
# excercise 6
# When installing anaconda on a student's computer, there's a 1 in 250 chance that 
# he download is corrupted and the installation fails. What are the odds that after 
# having 50 students download anaconda, no one has an installation issue? 100 students?
# What is the probability that we observe an installation issue within the first 
# 150 students that download anaconda?
# How likely is it that 450 students all download anaconda without an issue?


probability = 1/250
simulations = n_rows4 = 10_000
student_50 = n_cols4 = 50
student_100 = n_cols5 = 100
student_150 = n_cols6 = 150
student_450 = n_cols7 = 450


corrupt = np.random.random((n_rows4, n_cols4))
prob_corrupt = pd.DataFrame(corrupt)
are_corrupt_50 = prob_corrupt < probability
no_issues = (are_corrupt_50.sum(axis=1) == 0).mean()
print('odds that after having 50 students download anaconda, no one has an installation issue no_issues?', no_issues)

corrupt1 = np.random.random((n_rows4, n_cols5))
prob_corrupt1 = pd.DataFrame(corrupt1)
are_corrupt_100 = prob_corrupt1 < probability
no_issues1 = (are_corrupt_100.sum(axis=1) == 0).mean()
print('odds that after having 100 students, no issues', no_issues1)

corrupt2 = np.random.random((n_rows4, n_cols6))
prob_corrupt2 = pd.DataFrame(corrupt2)
are_corrupt_150 = prob_corrupt2 < probability
is_issue = (are_corrupt_150.sum(axis=1) ==0).mean()
print('probability that we observe an installation issue within the first # 150 students that download anaconda?', is_issue)

corrupt3 = np.random.random((n_rows4, n_cols7))
prob_corrupt3 = pd.DataFrame(corrupt3)
are_corrupt_450 = prob_corrupt3 < probability
no_issues2 = (are_corrupt_450.sum(axis=1) == 0).mean()
print('How likely is it that 450 students all download anaconda without an issue?', no_issues2)
# %%
# excercise 7
# There's a 70% chance on any given day that there will be at least one food truck at Travis Park.
# However, you haven't seen a food truck there in 3 days. How unlikely is this?
# How likely is it that a food truck will show up sometime this week?

simulations = np.random.choice(['food truck','no food truck'], p=[.7,.3], size=(10_000, 3))
(simulations == 'no food truck').all(axis=1).mean()
#%%
simulations1 = np.random.choice(['food truck','no foodruck'], p=[.7,.3], size=(10_000, 5))
(simulations1 == 'food truck').any(axis=1).mean()

# %%

# excercise 8
# if 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

