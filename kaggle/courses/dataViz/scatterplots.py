import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
candy_filepath = "../input/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath, index_col="id")


# Fill in the line below: Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?  (Please enclose your answer in single quotes.)
competitorWinPercent = lambda x: \
                        candy_data.loc[candy_data.competitorname == x]["winpercent"]\
                        .item()

more_popular = '3 Musketeers' \
    if competitorWinPercent('3 Musketeers') > competitorWinPercent('Almond Joy') \
    else 'Almond Joy'

# Fill in the line below: Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'? (Please enclose your answer in single quotes.)
more_sugar = 'Air Heads' \
    if candy_data.loc[candy_data.competitorname == 'Air Heads']["sugarpercent"].item() > \
    candy_data.loc[candy_data.competitorname == 'Baby Ruth']["sugarpercent"].item() \
    else 'Baby Ruth'


sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent']) # Your code here


# Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent'
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent']) # Your code here

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'],
               hue=candy_data['chocolate']) # Your code here


# Color-coded scatter plot w/ regression lines
sns.lmplot(x='pricepercent', y='winpercent',
               hue='chocolate', data=candy_data) # Your code here


# Scatter plot showing the relationship between 'chocolate' and 'winpercent'
sns.swarmplot(x=candy_data['chocolate'],
              y=candy_data['winpercent']) # Your code here


