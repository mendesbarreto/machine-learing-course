import pandas as panda
import numpy.random as random
import numpy
from pandas.core.generic import NDFrame

from dataset_cleaner import DataSetCleaner
import matplotlib.pyplot as pyplot

from sklearn.datasets import load_boston

report = open("report.txt", "w");

# Loading data set from science kit bosto
dataset = load_boston()

# Creating data frame to work with it
data_frame: NDFrame = panda.DataFrame(dataset.data, columns=dataset.feature_names)
data_frame['target'] = dataset.target

# Clean the data
data_frame_cleaner = DataSetCleaner()
data_frame = data_frame_cleaner.remove_empty_values(data_frame)

data_frame_correlation = data_frame.corr(method='pearson')
data_frame_correlation = data_frame_cleaner.remove_last_column(data_frame_correlation)




print(dataset.target)







