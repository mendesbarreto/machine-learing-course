import pandas
import numpy.random as random
import numpy
import matplotlib.pyplot as pyplot

PI = numpy.pi

NUMBER = 50

x = random.rand(NUMBER)
y = random.rand(NUMBER)

colors = random.rand(NUMBER)

area = PI * (15 * random.rand(NUMBER))**2
pyplot.scatter(x, y, s=area, c=colors, alpha=0.5)
pyplot.show()



