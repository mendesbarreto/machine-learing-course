import pandas as panda
import numpy.random as random
import numpy
import matplotlib.pyplot as pyplot
from pandas.core.generic import NDFrame


class DataSetCleaner:
    def remove_empty_values(self, data_frame: NDFrame) -> NDFrame:
        modified_data_set = data_frame.fillna(" ")
        sum_empty_values = panda.isnull(modified_data_set).sum()

        if sum_empty_values.any():
            print("Has some empties values in the data frame")
            raise Exception("Problem in load data set, we need to remove them")

        return modified_data_set

    def remove_last_column(self, data_frame: NDFrame) -> NDFrame:
        return data_frame.iloc[:-1, :-1]
