
import pandas as pd

file_path = 'adult.data.csv'
df = pd.read_csv(file_path)

aa= pd.read_csv(file_path, usecols=['native-country','salary'] )
bb= aa[aa['salary']=='>50K']
cc= bb['native-country'].value_counts()
gg = bb['native-country']
hh = gg.count()
dd= bb.idxmax()
ee = cc.max()

print(ee)

percen = (ee/hh)*100


h =pd.read_csv(file_path,usecols=['occupation','native-country','salary'])
a = h[h['native-country']=='India']
b= a[a['salary']=='>50K']
c = b['occupation'].value_counts()
d= c.idxmax()
e = c.max()
print(f'the Maximum number of occupation is {d} which is {e}')


min_hour = df['hours-per-week']
value = df[df['hours-per-week']== 1]
num_min_hour = len(value)

sal = value[value['salary']=='>50K']
num_sal = len(sal)

percentage = (num_sal/num_min_hour)*100
print(percentage)


work = df['hours-per-week']
cc= work.min()


low = df[df['education'].isin(['HS-grad','11th','9th','Some-college','Assoc-acdm','Assoc-voc','7th-8th','5th-6th','10th','1st-4th','Preschool','12th'])]
low_edu = len(low)
sal = low[low['salary']=='>50K']
sal_lin = len(sal)
percentage_low= (sal_lin/low_edu)*100
print("Percentage of people with not advanced education making more than 50K:", percentage_low)


col = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
num=len(col)
li = col[col['salary'] =='>50K']
lu = len(li)
percentage = (lu / num) * 100
print("Percentage of people with advanced education making more than 50K:", percentage)

edu = df['education']
v = (5355/edu.count())*100

males = df[df['sex'] == 'Male']
maless = males['age'].mean()

re = df['race']
seri = re.value_counts()

