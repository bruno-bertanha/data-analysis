import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2050, 1)
    y1 = lin1.slope * x1 + lin1.intercept
    plt.plot(x1, y1, 'r')

    # Create second line of best fit
    df_2 = df[df['Year'] >= 2000]

    lin2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000, 2050, 1)
    y2 = lin2.slope * x2 + lin2.intercept
    plt.plot(x2, y2, 'b')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()