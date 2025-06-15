import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Linear regression on all data
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series(range(1880, 2051))
    y_full = res_full.intercept + res_full.slope * x_full
    ax.plot(x_full, y_full, 'r', label='Best fit: all data')

    # Linear regression from year 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    ax.plot(x_recent, y_recent, 'g', label='Best fit: from 2000')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Legend
    ax.legend()

    # Save and return
    plt.savefig('sea_level_plot.png')
    return ax

