reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)


#other relevant code
df = reviews.loc[reviews.price.notnull()]
reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews.set_index("title")


#q1
#desc is a series
desc = reviews["description"]

#q2
first_description = desc.iloc[0]
first_description = reviews.description.iloc[0]
first_description = reviews.description.loc[0]
first_description = reviews.description[0]

#q3
first_row = reviews.iloc[0]

#q4
first_descriptions = reviews.description.iloc[:10]
first_descriptions = desc.head(10)
first_descriptions = reviews.loc[:9, "description"]

#q5
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8],:]
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]


#q6
df = reviews.loc[[0, 1, 10, 100],
                  ["country", "province", "region_1", "region_2"]]


#q7
df = reviews.loc[0:99,
                 ["country", "variety"]]

cols = ['country', 'variety']
df = reviews.loc[:99, cols]

cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]


#q8
italian_wines = reviews.loc[reviews.country == 'Italy']



#q9
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', "New Zealand"])) & 
    (reviews.points >= 95)
]





