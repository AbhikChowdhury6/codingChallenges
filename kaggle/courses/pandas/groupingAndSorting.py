

#q1
reviews_written = reviews.groupby('taster_twitter_handle').size()
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()



#q2
best_rating_per_price = reviews.groupby("price").points.max()

#q3
minPrices = reviews.groupby("variety").price.min().values
maxPrices = reviews.groupby("variety").price.max().values
#print(minPrices)

#ind = reviews.variety.unique()

ind = reviews.groupby("variety").apply(lambda x: x.variety.iloc[0])
#ind = ind.unique()

#print(ind)

price_extremes = pd.DataFrame({"min": minPrices, "max": maxPrices}, index=ind)

price_extremes = reviews.groupby('variety').price.agg([min, max])

#q4
sorted_varieties = price_extremes.sort_values(by=["min","max"], ascending=False)


#q5
reviewer_mean_ratings = reviews.groupby("taster_name").points.mean()


#q6
country_variety_counts = reviews.groupby(["country", "variety"]).variety.count().sort_values(ascending=False)
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)


