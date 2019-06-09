import numpy as numpy
import pandas as panda
import matplotlib.pyplot as plot
import seaborn as searborn
import os

dir_name = os.path.dirname(__file__)

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
rating_data_frame = panda.read_csv(dir_name + "/data/u.data",
                                   sep='\t',
                                   names=column_names)
rating_head_data_frame = rating_data_frame.head()

movie_titles_data_frame = panda.read_csv(dir_name + "/data/Movie_Id_Titles")
movie_titles_data_frame_head = movie_titles_data_frame.head()
data_frame = panda.merge(rating_data_frame, movie_titles_data_frame, on='item_id')

searborn.set_style('white')

grouped_ratings = data_frame.groupby('title')['rating']
grouped_ratings_average = grouped_ratings.mean()
top_rating_movies_data_frame = grouped_ratings_average.sort_values(ascending=False).head()
print(top_rating_movies_data_frame)

grouped_ratings_average_data_frame = panda.DataFrame(grouped_ratings_average)
grouped_ratings_average_data_frame['count'] = panda.DataFrame(grouped_ratings.count())

plot.figure(figsize=(10,4))
grouped_ratings_average_data_frame['count'].hist(bins=70)
plot.show()

plot.figure(figsize=(10,4))
grouped_ratings_average_data_frame['rating'].hist(bins=70)
plot.show()

searborn.jointplot(x='rating',
                   y='count',
                   data=grouped_ratings_average_data_frame,
                   alpha=0.5)
plot.show()

movie_mat = data_frame.pivot_table(index='user_id', columns='title', values='rating')
print(grouped_ratings_average_data_frame.sort_values('count', ascending=False).head(10))

star_wars_user_rating = movie_mat['Star Wars (1977)']
lier_lier_user_rating = movie_mat['Liar Liar (1997)']

print(star_wars_user_rating.head())

movies_like_star_wars = movie_mat.corrwith(star_wars_user_rating)
movies_like_lier_lier = movie_mat.corrwith(lier_lier_user_rating)

corr_starwars = panda.DataFrame(movies_like_star_wars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
print(corr_starwars.sort_values('Correlation', ascending=False).head(10))

corr_lier_lier = panda.DataFrame(movies_like_lier_lier, columns=['Correlation'])
corr_lier_lier.dropna(inplace=True)
corr_lier_lier = corr_lier_lier.join(grouped_ratings_average_data_frame['count'])

print(corr_lier_lier[corr_lier_lier['count'] > 100].sort_values('Correlation', ascending=False).head(10))

print("end of program")











