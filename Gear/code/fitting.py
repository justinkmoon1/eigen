import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


def fit_power(x, y):
    # Perform the curve fit
    popt, pcov = curve_fit(power_func, x, y, p0=[1.44, 0.35, 0.1], maxfev=5000)
    
    # Extract the optimized parameters
    a_opt, b_opt, c_opt = popt
    
    # Generate fitted values for plotting
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = power_func(x_fit, a_opt, b_opt, c_opt)
    
    # Calculate the predicted values of y using the fitted parameters
    y_predicted = power_func(x, a_opt, b_opt, c_opt)
    
    # Calculate adjusted R-squared (if needed)

    return {'x': x_fit, 'y': y_fit, 'coefficients': popt, 'predicted': y_predicted}


def power_func(x, a, b, c):
    print("parameters:", a, b, c)
    return a / (x + b) ** 2 + c


data = pd.read_excel("Gear\data\magnetic force fitting.xlsx")
yn = data['force']
x = data['dist']

# Filter data in the interval [2, 10]
mask = (x >= 2) & (x <= 10)
x_filtered = x[mask]
yn_filtered = yn[mask]

# Fit the power function to the filtered data
fit_result = fit_power(x_filtered, yn_filtered)

# Plotting
plt.scatter(x, yn, label='Original Data')
plt.plot(fit_result['x'], fit_result['y'], label='Fitted Function', color='red')
plt.xlabel('Distance (cm)')
plt.ylabel('Magnetic Force (N)')
plt.legend()
plt.title('Fitted Function for Magnetic Force')
plt.show()
