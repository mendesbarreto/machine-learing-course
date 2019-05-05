import pandas as panda
import numpy.random as random
import numpy
import matplotlib.pyplot as pyplot
from pandas.core.generic import NDFrame


def remove_last_column(data_frame: NDFrame) -> NDFrame:
    return data_frame.iloc[:-1, :-1]


def filter_value_from(data_frame: NDFrame, threshold: float, correlation_value_excluded=1.0):
    filtered_data_frame: NDFrame = data_frame[abs(data_frame) > threshold][data_frame != correlation_value_excluded]
    filtered_unstack = filtered_data_frame.unstack()
    filtered_dropna = filtered_unstack.dropna()
    return filtered_dropna.to_dict()


def remove_empty_values(data_frame: NDFrame) -> NDFrame:
    modified_data_set = data_frame.fillna(" ")
    sum_empty_values = panda.isnull(modified_data_set).sum()

    if sum_empty_values.any():
        print("Has some empties values in the data frame")
        raise Exception("Problem in load data set, we need to remove them")

    return modified_data_set
