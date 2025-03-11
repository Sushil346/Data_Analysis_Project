import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = np.where( (df['weight']/((df['height'] / 100) ** 2)) > 25 , 1, 0 )

# 3 Recorrecting cholesterol and glucose into good (0) abd bad (1)
df['cholesterol'] = np.where(df['cholesterol']>1, 1, 0)
df['gluc'] = np.where(df['gluc']>1, 1, 0)


# 4
def draw_cat_plot():
    df_cat = df[['age', 'cholesterol']]  # Ensure 'age' and 'cholesterol' are correct column names
    fig = sns.catplot(x="age", hue="cholesterol", data=df_cat, kind='box')  # Use 'age' not 'Age'
    
    # Set axis labels and title
    fig.set_axis_labels('Age', 'Cholesterol')
    fig.fig.suptitle('Age VS Cholesterol')
    
    # Save the plot
    fig.savefig('catplot.png')
    
    # Show the plot
    plt.show()

    return fig


##################################################################
    
# 5  Melting and value_vars = ['cholesterol', 'gluc','smoke','alco','active', 'overweight'], var_name='Indicator', value_name= 'value'

df_cat = df_cat = pd.melt(df,id_vars=df.columns[:6] ,value_vars = ['cholesterol', 'gluc','smoke','alco','active', 'overweight'], var_name='Indicator', value_name= 'value')


# 6 Melting and grouping based on cardio making cardio id and value vars are cholesterol .... and also counting the total no of similar state
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# Group the data by 'cardio' and count occurrences of each feature
df_cat_grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')

# Rename the 'value' column to 'feature_value' to avoid conflicts for catplot
df_cat_grouped = df_cat_grouped.rename(columns={'value': 'feature_value'})

# Show the resulting DataFrame
print(df_cat_grouped)


# 7 
fig1 = sns.catplot(x='variable', y='count', hue='feature_value', data=df_cat_grouped, kind='bar', col='cardio')


# 8
fig=fig1.fig


# 9
fig.savefig('catplot.png')


# 10
def draw_heat_map():

    # 11
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    
    # Filter out rows where height is less than the 2.5th percentile or more than the 97.5th percentile
    height_lower = df_heat['height'].quantile(0.025)
    height_upper = df_heat['height'].quantile(0.975)
    df_heat = df_heat[(df_heat['height'] >= height_lower) & (df_heat['height'] <= height_upper)]
    
    # Filter out rows where weight is less than the 2.5th percentile or more than the 97.5th percentile
    weight_lower = df_heat['weight'].quantile(0.025)
    weight_upper = df_heat['weight'].quantile(0.975)
    df_heat = df_heat[(df_heat['weight'] >= weight_lower) & (df_heat['weight'] <= weight_upper)]


    # 12
    corr =  df.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu', square=True, mask=mask, 
                cbar=True, linewidths=0.5, linecolor='white', ax=ax)
    ax.set_title("Correlation Heatmap")
    
       
    # 15 //correlation also done in 14


    # 16
    fig.savefig('heatmap.png')
    
    return fig
