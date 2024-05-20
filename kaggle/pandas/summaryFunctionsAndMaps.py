import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)


#q1
median_points = reviews.points.median()


#q2
countries = reviews.country.unique()


#q3
reviews_per_country = reviews.country.value_counts()

#q4
centered_price = reviews.price.map(lambda x: x - reviews.price.mean())


#q5
reviews["points to price ratio"] = reviews.points / reviews.price
bargain_wine = reviews.loc[
    reviews["points to price ratio"] == reviews["points to price ratio"].max(),
    ["title"]
].iloc[0]["title"]
print(bargain_wine)

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#q6
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])


#q7
star_ratings = pd.Series(
    reviews[["points", "country"]].apply(
        (lambda x: 
        3 if x["points"] >= 95 or x["country"] == "canada" 
        else 2 if x["points"] >= 85 
        else 1
    ), axis=1)
)
