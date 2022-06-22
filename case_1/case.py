#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('st.csv')
#print(df)
print(df.info())





#print(df.describe())
#cумма баллов
df['Summa'] = df['math score'] + df['reading score']+df['writing score']


#сводная таблица
temp = df.pivot_table(index = 'parental level of education', columns = 'test preparation course', values = 'Summa', aggfunc ='mean')
print(temp)





print('Максимальная разность баллов  ',round(max(temp['completed']-temp['none'])))
#
print(round(df.groupby(by = 'test preparation course')['Summa'].mean()))
#
print(round(df.groupby(by = ['test preparation course','parental level of education'])['Summa'].mean()))

#df['Summa'].plot(kind = 'hist', bins = 7)
#df['test preparation course'].value_counts().plot(kind = 'pie')

#df['parental level of education'].value_counts().plot(kind = 'bar',grid = True)

#df['gender'].value_counts().plot(kind = 'pie')

temp.plot(kind = 'barh', grid = True)

plt.show()

min_b=df["Summa"].min()
print('Минимальный балл = ',min_b)
print(df[df['Summa']<min_b])
#группировка
print(round(df.groupby(by = 'parental level of education')["Summa"].mean()))
