import numpy as np
from fitting_functions import*
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
data = np.loadtxt("tips.csv", delimiter=",", dtype=str)
print(data)
x = data[1:,0].astype(np.float32)
y= data[1:, 1].astype(np.float32)
print("y = ", y)
print("x = ", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
x_units='dollars'
y_units='dollars'
print_equation(slope,intercept,y_units,x_units)
##output was The equation of the line is:y= 0.18221473222560391 dollar/dollar + -0.2922674195507699 dollar
fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("Bill") #change the units as appropriate
plt.ylabel("Tips")  #change the units as appropriate
plt.show()
fig.savefig('plot_tips.png')
x = data[1:,0].astype(np.float32)
y= data[1:, 6].astype(np.float32)
print("y = ", y)
print("x = ", x)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
x_units='dollars'
y_units='%'
print_equation(slope,intercept,y_units,x_units)
fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("Bill") #change the units as appropriate
plt.ylabel("PctTip")  #change the units as appropriate
plt.show()
fig.savefig('plot_perc.png')
