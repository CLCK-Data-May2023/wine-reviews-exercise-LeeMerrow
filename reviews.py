# add your code here
import pandas as pd

reviews = pd.read_csv('data\winemag-data-130k-v2.csv.zip', index_col=0)

reviews_per_country = reviews.country.value_counts()

reviews_points = reviews.groupby('country')['points'].mean().round(1)

reviews_merge = pd.DataFrame.merge(reviews_per_country, reviews_points, on='country', how='inner')

with open('data\\reviews-per-country.csv', 'w') as csv_file:
    reviews_merge.to_csv(path_or_buf=csv_file)
