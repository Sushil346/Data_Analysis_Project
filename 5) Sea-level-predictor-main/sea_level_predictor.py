import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col=0)

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df.index, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    ## y = w*X + b ; w= slope, b= yintercept
    calculated_df = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    x_value = np.concatenate([df.index, np.arange(2014,2051)])
    y_value = (calculated_df.slope * x_value) + calculated_df.intercept
    ax.plot(x_value,y_value,'r')

    # Create second line of best fit
    calc_recent = linregress(df.index[df.index >= 2000], df[df.index >= 2000]['CSIRO Adjusted Sea Level'])
    x_value2 = np.concatenate([df.index[df.index >= 2000], np.arange(2014, 2051)])
    y_value2 = (calc_recent.slope * x_value2) + calc_recent.intercept
    ax.plot(x_value2, y_value2, 'g')


    # Add labels and title
    ax.set(
    xticks=list(range(1850,2100,25)),title="Rise in Sea Level",
    xlabel="Year",ylabel="Sea Level (inches)" 
    )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()