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

sns.barplot(data=df, x=toothpicks_intersected)