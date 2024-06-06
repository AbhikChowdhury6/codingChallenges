import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

#q1
# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)


#q2
home_data.describe()

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = round(home_data.LotArea.mean())

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 2024 - home_data.YearBuilt.max()