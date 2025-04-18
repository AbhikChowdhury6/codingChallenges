# Code you have previously used to load data
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)

#p1
print(home_data.columns)


y = home_data.SalePrice


#p2
# Create the list of features below
feature_names = ["LotArea",
                 "YearBuilt",
                 "1stFlrSF",
                 "2ndFlrSF",
                 "FullBath",
                 "BedroomAbvGr",
                 "TotRmsAbvGrd"]

# Select data corresponding to features in feature_names
X = home_data[feature_names]

#p3
from sklearn.tree import DecisionTreeRegressor
#specify the model. 

#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X,y)

#p4
predictions = iowa_model.predict(X)
print(predictions)

print(predictions[:5])
print(y.head(5))
print(X.head(5))
