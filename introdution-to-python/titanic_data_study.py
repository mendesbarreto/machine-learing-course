import pandas as panda
from rpy2.robjects import r
import rpy2.robjects.pandas2ri as pandas2ri
import numpy as numpy
import matplotlib.pyplot as pyplot
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

file_data_set = "/Users/mendesbarreto/Git/machine-learing-course/introdution-to-python/data/titanic.raw.rdata"
reference_to_data_set_from_r_data = r['load'](file_data_set)
dataset = r['titanic.raw']
panda_data_frame = pandas2ri.ri2py_dataframe(r['titanic.raw'])

records = []
for colum in range(0, 2201):
    records.append([str(panda_data_frame.values[colum, row]) for row in range(0, 4)])

transaction_encoder = TransactionEncoder()
transaction_encoder_array = transaction_encoder.fit(records).transform(records)
data_frame = panda.DataFrame(transaction_encoder_array, columns=transaction_encoder.columns_)
frequent_itemsets = apriori(data_frame, min_support=0.3, use_colnames=True)

association_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
association_rules = association_rules

association_rules.plot()
pyplot.show()
#  Test libs
# file_data_set = "/Users/mendesbarreto/Git/machine-learing-course/introdution-to-python/data/titanic.raw.rdata"
# reference_to_data_set_from_r_data = r['load'](file_data_set)
# dataset = r['titanic.raw']
# panda_data_frame = pandas2ri.ri2py_dataframe(r['titanic.raw'])

# records = []
# for colum in range(0, 2201):
#     records.append([str(panda_data_frame.values[colum, row]) for row in range(0, 4)])

# association_rules = apriori(records, 0.32)
# association_rules_results = list(association_rules)
#
# first_rules = association_rules_results[1]
#
# print("First Rule")
# print(first_rules)

print("END")