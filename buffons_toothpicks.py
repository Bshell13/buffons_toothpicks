"""
Buffon's "Toothpick" Experiment

Brandon Shellenberger

This project is for my students to discover Buffon's Needle Experiment.
I will gather all the data from what my students have made.
"""

# Import Libraries
import math
import statistics as stat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("test.csv")

print(df.head())

print(df.describe())

sns.barplot(data=df, x='block', y='toothpicks_intersected')
plt.ylabel('Avgerage Toothpicks Intersected')
plt.xlabel('Block')
plt.title('Average Toothpicks Intersecting Lines per Block')
plt.show()

#Finding the probability
prob = (len(df['toothpicks_intersected']) * 10) / df['toothpicks_intersected'].sum() * 2

print(f'The probability of a toothpick landing on a line is: {prob}')

#plotting the theoretical value.
total_intersected = 0
total = 0
df['theoretical_value'] = 0
for index in range(0,len(df['toothpicks_intersected'])):
    total += 10
    total_intersected += df['toothpicks_intersected'][index]
    df['theoretical_value'][index] = (total / total_intersected) * 2

sns.lineplot(data=df, x=df.index, y='theoretical_value')
plt.xlabel('Order of Records Inputted')
plt.ylabel('Theoretical Probability')
plt.title('Theoretical Probability of Toothpicks Intersecting')
plt.show()