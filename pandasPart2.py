import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

# head method returns data of top 5 rows
print('Head method returns data of top 5 entries\n\n', df.head(), '\n\n\n')

# returns first 20 entries of data
print('Head method with 20 returns data of top 20 entries\n\n', df.head(20), '\n\n\n')

# tail method return data of bottom 5 rows
print('Tail method returns data of bottom 5 entries\n\n', df.tail(), '\n\n\n')

# The info() function is used to get essential information about your dataset, such as number of rows, columns, data types, etc:
print('Info method returns the info of dataset\n\n ')
df.info()
# We also see that Pandas has added an auto generated index.
# We can set our own index column by using the set_index() function:
df.set_index("date", inplace=True)
print('\n\n',df.head(), '\n\n\n')

# The inplace=True argument specifies that the change will be applied to our DataFrame, without the need to assign it to a new DataFrame variable.


# Since our data is only for the state of California, we can remove that column from our DataFrame, as it contains the same value for all rows:
df.drop('state', axis=1, inplace=True)
print('\n\n', df.head(),'\n\n\n')
# df.info()
# df.iloc[-1] will find the last value of the dataset
print(df.iloc[-1])
# drop() deletes rows and columns.
# axis=1 specifies that we want to drop a column.
# axis=0 will drop a row.