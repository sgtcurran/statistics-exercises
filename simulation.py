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
#divid 
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

data_scinece = .25 
n_sim= nrows3 = 10_000 
n_cohorts = ncols3 = 2

cohorts = np.random.random((n_sim * n_cohorts)).reshape(nrows3, ncols3)
prob_data = pd.DataFrame(cohorts)
select_data = prob_data < data_scinece
select_data

# %%
