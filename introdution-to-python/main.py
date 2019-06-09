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

head = grouped_ratings_average_data_frame.head()

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

print("end of program")








