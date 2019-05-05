import matplotlib
import pandas as panda
import numpy.random as random
import numpy
from pandas.core.generic import NDFrame
import seaborn
from dataset_cleaner import *
import matplotlib.pyplot as pyplot

from sklearn.datasets import load_boston


report = open("report.txt", "w");

# Loading data set from science kit bosto
dataset = load_boston()

# Creating data frame to work with it
data_frame: NDFrame = panda.DataFrame(dataset.data, columns=dataset.feature_names)
data_frame['target'] = dataset.target

# Clean the data
data_frame = remove_empty_values(data_frame)

data_frame_correlation = data_frame.corr(method='pearson')
data_frame_correlation = remove_last_column(data_frame_correlation)

description = load_boston()['DESCR']
print(description)

# This value describe the minimum value of approximation
threshold = .5
correlation_number_not_allowed = 1.0

relevant_correlation = filter_value_from(data_frame_correlation,
                                        threshold,
                                        correlation_number_not_allowed)



unique_important_corrs = panda.DataFrame(
    list(set([(tuple(sorted(key)), relevant_correlation[key])
         for key in relevant_correlation])), columns=['attribute pair', 'correlation'])
# sorted by absolute value
print(unique_important_corrs)

unique_important_corrs: NDFrame = unique_important_corrs.ix[
    abs(unique_important_corrs['correlation']).argsort()[::-1]]

print("Paires de correlation:")
print(unique_important_corrs)





