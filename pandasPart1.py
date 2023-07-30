# Pandas is one of the most popular data science libraries in Python. Easy to use, it is built on top of NumPy and shares many functions and properties.

# With Pandas, you can read and extract data from files, transform and analyze it, calculate statistics and correlations, and much more!

# To start using pandas, we need to import it first:
import pandas as pd
# The two primary components of pandas are the Series and the DataFrame.

# A Series is essentially a column, and a DataFrame is a multi-dimensional table made up of a collection of Series.

# For example, the following DataFrame is made of two Series, ages and heights

# Before working with real data, let's first create a DataFrame manually to explore its functions.
# The easiest way to create a DataFrame is using a dictionary:

# ------------------------------------
data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}
print(data,'\n\n')
# ------------------------------------
# Each key is a column, while the value is an array representing the data for that column.
# Now, we can pass this dictionary to the DataFrame constructor:

# ------------------------------------
df = pd.DataFrame(data)
print(df)
# ------------------------------------

# ------------------------------------
# x = {
# 'a': [1, 2],
# 'b': [3, 4],
# 'c': [5, 6]
# }
# df = pd.DataFrame(x)
# print(df)
# ------------------------------------

# The DataFrame automatically creates a numeric index for each row.
# We can specify a custom index, when creating the DataFrame:
# ------------------------------------
# df = pd.DataFrame(data, index=['Ali', 'Aslam', 'Asif', 'Zia'])
# print('\n\n', df)
# ------------------------------------
# We can select a single column by specifying its name in square brackets:
# print('\n\nSelect particular column (series)\n',df['ages'])


# print('\n\n', df[['ages', 'heights']])
# slicing
print('\n\n\n')
print(df.iloc[2])
print('\n',df.iloc[:3])
print('\n',df.iloc[0:3])
print('\n',df.iloc[-2:])

# conditionals
print( df[ (df['ages']>18) & (df['heights']>180) ] )