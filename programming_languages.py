# -*- coding: utf-8 -*-
""" # A Data-Driven Analysis of the Popularity of Different Programming Languages over Time

Get the Data Either use the provided .csv file or (optionally) get fresh (the freshest?)
data from running an SQL query on StackExchange: """

# Import Statements
import pandas as pd
import matplotlib.pyplot as plt

""" Data Exploration """
# Read the .csv file and store it in a Pandas dataframe
df = pd.read_csv('QueryResults.csv', names= ['DATE', 'TAG', 'POSTS'], header=0 )

# Display the first 5 rows and last 5 rows of the dataframe
df.head()
df.tail()

# Check how many rows and how many columns there are or the shape of the dataframe.
df.shape

"""Count the number of entries in each column of the dataframe"""
df.count()

"""The total number of post per language."""
df.groupby('TAG').sum()

"""Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.
Find how many months of data exist per language? Which language had the fewest months with an entry? """
df.groupby('TAG').count()

""" Data Cleaning
 Use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01 """

df['DATE'][1]
df.DATE[1]

type(df.DATE[1])

print(pd.to_datetime(df.DATE[1]))
type(pd.to_datetime(df.DATE[1]))

# Convert Entire Column
df.DATE = pd.to_datetime(df.DATE)
df.head()

""" Data Manipulation """
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
test_df

"""Convert DataFrame each category has its own column. The easiest way to accomplish this is by using the **.pivot()** method in Pandas."""
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
pivoted_df

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df

"""Dimensions of new dataframe and the column names."""
reshaped_df.shape
reshaped_df.columns

"""When we count the number of entries per column we see that not all languages are the same. The reason is that the .count() method excludes NaN values. When we pivoted the DataFrame the NaN values were inserted when there were no posts for a language in that month (e.g., Swift in July, 2008)."""
reshaped_df.head()

"""Count the number of entries per programming language that might be different."""
reshaped_df.count()

"""**Dealing with NaN Values**
In this case, we don't want to drop the rows that have a NaN value. Instead, we want to substitute the number 0 for each NaN value in the DataFrame. We can do this with the .fillna() method.
"""

reshaped_df.fillna(0, inplace=True)

"""The inplace argument means that we are updating reshaped_df.

Without inplace argument
"""

reshaped_df = reshaped_df.fillna(0)

reshaped_df.head()

"""**Look for NaN values in the dataframe:**

Here using the .isna() method, also  the values attribute and the any() method. This means we don't have to search through the entire DataFrame to spot if .isna() is True.
"""

reshaped_df.isna().values.any()

"""## Data Visualisaton with with Matplotlib

Using the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.
"""

plt.plot(reshaped_df.index, reshaped_df.java)

"""Square bracket notation."""

plt.plot(reshaped_df.index, reshaped_df['java'])

"""**Styling the Chart**

Let's look at a couple of methods that will help us style our chart:

To make chart size increase
"""

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.plot(reshaped_df.index, reshaped_df.java)

"""Add labels and set a lower limit of 0 for the y-axis with .ylim()."""

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)

"""Python and  Java on the same chart."""

plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)

"""All the programming languages on the same chart"""

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column])

"""Add labels and legend to chart"""

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

"""Looks like Python is the most popular programming language judging by the number of posts on Stack Overflow! Python for the win!

# Smoothing out Time Series Data
Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html).
"""

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(reshaped_df.index, roll_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(reshaped_df.index, roll_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

roll_df = reshaped_df.rolling(window=3).mean()

plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(reshaped_df.index, roll_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)