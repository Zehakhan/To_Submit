
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


file_path = 'epa_sea_level.csv'
df = pd.read_csv(file_path)


plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data points')


slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])


years_extended = pd.Series(range(df['Year'].min(), 2051))


sea_levels_predicted = intercept + slope * years_extended


plt.plot(years_extended, sea_levels_predicted, 'r', label='Best fit line (all data)')


df_recent = df[df['Year'] >= 2000]


slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])


sea_levels_predicted_recent = intercept_recent + slope_recent * years_extended


plt.plot(years_extended, sea_levels_predicted_recent, 'g', label='Best fit line (2000 onwards)')


plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')


plt.legend()


plt.grid(True)


plt.savefig('sea_level_rise.png')


plt.show()









