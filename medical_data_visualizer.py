import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np





file_path = ('medical_examination.csv')
df  = pd.read_csv(file_path)
df['height'] = (df['height'])/100
df['BMI'] = (df['weight'])/(df['height'] **2)
df['overweight'] = (df['BMI'] > 25).astype(int)


df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


categorical_features = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']


df_long = pd.melt(df, id_vars=['cardio'], value_vars=categorical_features, 
                  var_name='variable', value_name='value')


g = sns.catplot(
    x='variable', 
    hue='value', 
    col='cardio', 
    data=df_long, 
    kind='count',
    height=5, 
    aspect=1.5,
    palette='tab10'
)


g.set_axis_labels("Value", "Count")
g.set_titles("Cardio = {col_name}")
g.despine(left=True)
plt.show()

(df['ap_lo'] <= df['ap_hi'])
(df['height'] >= df['height'].quantile(0.025))
(df['weight'] >= df['weight'].quantile(0.025))
(df['height'] <= df['height'].quantile(0.975))

(df['weight']>=df['weight'].quantile(0.975))

correlation_mat = df.corr()
mask = np.triu(np.ones_like(correlation_mat, dtype=bool))



sns.heatmap(correlation_mat,mask=mask,annot=True,cmap='coolwarm',fmt='.2f')
plt.show()