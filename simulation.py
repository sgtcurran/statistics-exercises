#%%
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
import viz


# %%
n_trials = nrows = 10_000
n_dice = ncols = 3

rolls = np.random.choice([1, 2, 3, 4, 5, 6], n_trials * n_dice).reshape(nrows, ncols)
rolls

# %%
sums_by_trial = rolls.sum(axis=1)
sums_by_trial

viz.simulation_example1(sums_by_trial)

# %%
n_trials1 = nrows1 = 10_000
n_dice1 = ncols1 = 2

rolls_dice = np.random.choice([1,2,3,4,5,6], n_trials1 * n_dice1).reshape(nrows1, ncols1)
double = pd.DataFrame(rolls_dice)
double


# %%
