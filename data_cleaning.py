import pandas as pd
dataset = pd.read_csv("covid_dataset_updated.csv")
print(dataset)

# first we check does any column contains any null value
print(dataset.isnull())
# here true will represent null values

# now counting missing values
print(dataset.isnull().sum())

# here cases contains 53 null values and deaths contain 56 null values
# now we will drop i.e delete missing values in particular tables
dataset_with_deleted_duplicates = dataset.dropna()

# note: if you want to in same dataframe of dataset rather than creating a new dataframe then just use inplace keyword
# dataset.dropna(inplace=True)

# dropna() is used to delete data from a dataset which contain empty values
print(dataset_with_deleted_duplicates.isnull().sum())

dataset_with_deleted_duplicates.info()

print(dataset_with_deleted_duplicates)

# now we will fill missing data in the dataframe
# we will use fillna method to fill empty data in dataset
print(dataset['Cases'].isnull())

data_filled_with_zero = dataset.fillna(0)
print(data_filled_with_zero)
# it will put only zero at place where data is empty

print(data_filled_with_zero.head(50))

# now we will fill data mean value i.e average value in missing cells.
data_filled_with_avg_value = dataset.fillna(dataset[['Cases', 'Deaths']].mean())
print(data_filled_with_avg_value.head(20))

# now we will remove duplicated data in our dataset
# we will use .duplicated method to do this task
dataset = pd.read_csv("covid_dataset_updated.csv")
print(dataset.duplicated().head(50))


print(dataset.duplicated().sum())

# sorting data
sorted_dataset = dataset.sort_values(by="Date")
print(sorted_dataset)


sorted_dataset = dataset.sort_values(by="Date", ascending=False)
print(sorted_dataset)

# for creaing a new csv file
dataset.to_csv("updated file.csv")
