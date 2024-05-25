import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")

my_filepath = "/kaggle/input/cyclistic-bike-share/Divvy_Trips_2020_Q1/Divvy_Trips_2020_Q1.csv"

my_data = pd.read_csv(my_filepath, index_col="ride_id")

len(pd.to_datetime(my_data["started_at"]).dt.strftime('%H:%M').unique())

sns.histplot(data=pd.to_datetime(my_data["started_at"]).dt.strftime('%H')) # Your code here
