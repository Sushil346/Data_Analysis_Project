import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col = 'date')

# Clean data
low_data = df['value'].quantile(0.025)
high_data = df['value'].quantile(0.975)

df = df[ (df['value']>=low_data) & (df['value']<=high_data) ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df['value'], color='r', linewidth = 1 )
    ax.set_title ("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    plt.tight_layout()
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month

    fig, ax = plt.subplots(figsize=(8, 7))
    month_colors = sns.color_palette("tab10", 12)

    plt.figure(figsize=(8,7))
    sns.barplot(data=df, x='year', y='value', hue='month', palette=month_colors)

    ax.set_xlabel("Year")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Monthly Page Views for Multiple Years")
    

    # Show the plot
    plt.tight_layout()
    plt.show()



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


import calendar

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df['year'] = df.index.year
    df['month'] = df.index.month

    df['month_name'] =  df.index.strftime('%b')

    fig, axes= plt.subplots(1, 2, figsize=(14,7))

    sns.boxplot(ax=axes[0], x='year', y='value',hue='year' , data= df, palette='Set2')
    axes[0].set_title("Year-wise Box Plot (trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(ax=axes[1], x='month', y='value',hue='month', data=df, palette='Set3') #hue is kept just to make 
    axes[1].set_title("Month-wise Box Plot (trend)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.tight_layout()
    plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
