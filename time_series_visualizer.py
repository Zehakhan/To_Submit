
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
file_path = ('fcc-forum-pageviews.csv')
df = pd.read_csv(file_path,index_col='date',parse_dates=True)


lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)


df_cleaned = df[(df['value'] >= lower) & (df['value'] <= upper)]
df_copy = df_cleaned.copy(deep=True)

def draw_line_plot():
    
     plt.plot(df_copy.index, df_copy['value'], color='blue', linestyle='-', linewidth=2)
     plt.show()

df_copy['year']= df_copy.index.year
df_copy['month'] = df_copy.index.month

group = df_copy.groupby(['year','month'])['value'].mean().reset_index()

def draw_bar_plot():
     sns.barplot(data=group, x = 'year',y='value',hue="month",palette='tab10')
     plt.title('Monthly Average Page Views per Year')
     plt.xlabel('Years')
     plt.ylabel('Average Page Views')
     plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
     plt.tight_layout()
     plt.show()
     

def draw_box_plot():
     fig,axes = plt.subplots(1,2,figsize=(15,7))
     sns.boxplot(x='year',y='value',data=group,ax=axes[0])
     axes[0].set_title('Year-wise Box Plot (Trend)')
     axes[0].set_xlabel('Year')
     axes[0].set_ylabel('Page Views')

     sns.boxplot(x='Year',y='value',data=group,ax=axes[1],order=['jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
     axes[1].set_title('Month-wise Box Plot (Seasonality)')
     axes[1].set_xlabel('Month')
     axes[1].set_ylabel('Page Views')

     plt.tight_layout()
     plt.show()