import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# Fill in the line below: What is the highest average score received by PC games,
# for any genre?
high_score = max(ign_data.loc["PC"])

# Fill in the line below: On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = min(ign_data.loc["PlayStation Vita"].index, 
                  key = lambda x: ign_data.loc["PlayStation Vita"][x])


my_plot = sns.barplot(x=ign_data.index, y=ign_data['Racing']) # Your code here

my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=90)


# Heatmap showing average game score by platform and genre
my_plot = sns.heatmap(data=ign_data, annot=True) # Your code here

my_plot.set_xticklabels(my_plot.get_xticklabels(), rotation=90)
