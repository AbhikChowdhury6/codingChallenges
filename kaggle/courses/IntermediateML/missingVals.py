import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('../input/train.csv', index_col='Id')
X_test_full = pd.read_csv('../input/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)
                        
# Shape of training data (num_rows, num_columns)
print(X_train.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

#p1
# Fill in the line below: How many rows are in the training data?
num_rows = y_train.shape[0]

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = len([1 for c in X_train.columns if X_train[c].isnull().any()])

# Fill in the line below: How many missing entries are contained in 
# all of the training data?
print([X_train[c].isnull().sum() for c in X_train.columns])
tot_missing = sum([X_train[c].isnull().sum() for c in X_train.columns])

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)


#p2

# Fill in the line below: get names of columns with missing values
colsToDrop = missing_val_count_by_column[missing_val_count_by_column > 0].index # Your code here

# Fill in the lines below: drop columns in training and validation data
reduced_X_train = X_train.drop(colsToDrop, axis=1)
reduced_X_valid = X_valid.drop(colsToDrop, axis=1)

print("MAE (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

#p3
from sklearn.impute import SimpleImputer

# Fill in the lines below: imputation
my_imputer = SimpleImputer() # Your code here
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Fill in the lines below: imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

#step 4
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp = IterativeImputer(max_iter=10, random_state=0)
# Preprocessed training and validation features
final_X_train = pd.DataFrame(imp.fit_transform(X_train))
final_X_valid = pd.DataFrame(imp.transform(X_valid))

# Define and fit model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)

# Get validation predictions and MAE
preds_valid = model.predict(final_X_valid)
print("MAE (Your approach):")
print(mean_absolute_error(y_valid, preds_valid))

# Fill in the line below: preprocess test data
final_X_test = pd.DataFrame(imp.transform(X_test))

# Fill in the line below: get test predictions
preds_test = model.predict(final_X_test)