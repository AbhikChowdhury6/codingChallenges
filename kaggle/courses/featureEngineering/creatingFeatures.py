import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor


def score_dataset(X, y, model=XGBRegressor()):
    # Label encoding for categoricals
    for colname in X.select_dtypes(["category", "object"]):
        X[colname], _ = X[colname].factorize()
    # Metric for Housing competition is RMSLE (Root Mean Squared Log Error)
    score = cross_val_score(
        model, X, y, cv=5, scoring="neg_mean_squared_log_error",
    )
    score = -1 * score.mean()
    score = np.sqrt(score)
    return score


# Prepare data
df = pd.read_csv("../input/fe-course-data/ames.csv")
X = df.copy()
y = X.pop("SalePrice")

# YOUR CODE HERE
X_1 = pd.DataFrame()  # dataframe to hold new features

features = ["WoodDeckSF", "OpenPorchSF", "EnclosedPorch",
            "Threeseasonporch", "ScreenPorch"]

X_1["LivLotRatio"] = X["GrLivArea"] / X["LotArea"]
X_1["Spaciousness"] = (X["FirstFlrSF"] + X["SecondFlrSF"]) / X["TotRmsAbvGrd"]
X_1["TotalOutsideSF"] = X[features].sum(axis=1)


# YOUR CODE HERE
# one hot encoded DF multiplied by another category
# One-hot encode BldgType. Use `prefix="Bldg"` in `get_dummies`
X_2 = pd.get_dummies(X.BldgType, prefix="Bldg") 
# Multiply
X_2 = X_2.mul(X.GrLivArea, axis=0)

X_3 = pd.DataFrame()

features = ["WoodDeckSF", "OpenPorchSF", "EnclosedPorch",
            "Threeseasonporch", "ScreenPorch"]

# YOUR CODE HERE
X_3["PorchTypes"] = X[features].gt(0.0).sum(axis=1)


X_3 = pd.DataFrame()

features = ["WoodDeckSF", "OpenPorchSF", "EnclosedPorch",
            "Threeseasonporch", "ScreenPorch"]

# YOUR CODE HERE
X_3["PorchTypes"] = X[features].gt(0.0).sum(axis=1)


X_4 = pd.DataFrame()

# YOUR CODE HERE
# X_4[['MSClass', "toDrop"]] = df.MSSubClass.str.split("_",n=1, expand=True)
# X_4 = X_4.drop("toDrop", axis=1)

X_4['MSClass'] = df.MSSubClass.str.split("_",n=1, expand=True)[0]


X_5 = pd.DataFrame()

# YOUR CODE HERE
X_5["MedNhbdArea"] = X.groupby("Neighborhood")["GrLivArea"].transform("median")
