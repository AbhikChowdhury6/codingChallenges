# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("../input/earthquake-database/database.csv")

# set seed for reproducibility
np.random.seed(0)

earthquakes.head()

earthquakes["Date"].head()

earthquakes[3378:3383]


date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()

indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
earthquakes.loc[indices]

earthquakes["Date"].loc[indices] = pd.to_datetime(earthquakes["Date"].loc[indices]).dt.strftime("%m/%d/%Y")

earthquakes.loc[indices]


earthquakes["earthquakes"] = pd.to_datetime(earthquakes["Date"], format = "%m/%d/%Y")

day_of_month_earthquakes = earthquakes["date_parsed"].dt.day

sns.distplot(day_of_month_earthquakes, kde=False, bins=31)

sns.barplot(x=earthquakes["Date"].groupby(day_of_month_earthquakes).count().index,
            y= earthquakes["Date"].groupby(day_of_month_earthquakes).count())











