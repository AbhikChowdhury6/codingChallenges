import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)


#q1
renamed = reviews.rename(columns={"region_1": "region", "region_2": "locale"})



#q2
reindexed = reviews.rename({"index": "wines"})
reindexed = reviews.rename_axis('wines', axis='rows')



#q3 prep
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

#q3
combined_products = pd.concat([gaming_products, movie_products])


#q4 prep
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

#q4
powerlifting_combined = powerlifting_competitors.set_index('MeetID').join(powerlifting_meets.set_index('MeetID'))


