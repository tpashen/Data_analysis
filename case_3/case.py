#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('menu.csv')

print(df.info())
df['Trans Fat']=df['Trans Fat'].apply(str)
df['Calories from Fat']=df['Calories from Fat'].apply(str)
pd.isnull(df)
temp = df.pivot_table(index = 'Category', columns = 'Trans Fat', values = 'Calories from Fat', aggfunc ='count')
print(temp)


temp.plot(kind = 'barh', grid = True)

plt.show()








