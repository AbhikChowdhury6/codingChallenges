import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#q1
dtype = reviews.points.dtype

#q2
point_strings = reviews.points.astype("str")



#q3
n_missing_prices = len(reviews[reviews.price.isnull() == True].price)

missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()


#q4
print(len(reviews[reviews.region_1.isnull() == True].region_1))

print(reviews.region_1.fillna("Unknown"))

print(reviews.region_1)

print(len(reviews[reviews.region_1.isnull() == True].region_1))

reviews_per_region = reviews.fillna("Unknown").groupby("region_1").region_1.count().sort_values(ascending=False)

print(reviews_per_region)


reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
