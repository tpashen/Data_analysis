#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries.csv')

print(df.info())


print(pd.isnull(df))


#print(pd.isnull(df['GDP ($ per capita)']))
# удаление пустых данных
df.dropna()
#print(pd.isnull(df['GDP ($ per capita)']))
mean_GDP=df['GDP ($ per capita)'].mean()
print('Минимальный ВВП ', mean_GDP)
temp=df[df['GDP ($ per capita)']<mean_GDP][['Country','GDP ($ per capita)','Literacy (%)']].head(10)
print(temp)
#перевод в целое число
df['Literacy (%)']=df['Literacy (%)'].apply(str)
mean_Literacy=df['Literacy (%)'].min()
m=df['Population'].min()
print()
print('Минимальная грамотность',mean_Literacy)
print(df[df['Literacy (%)']==mean_Literacy]['Country'])


#print(df.groupby(by = 'Country')['Literacy (%)'].min())
#print(df.groupby(by = 'Country')['GDP ($ per capita)'].agg(['min', 'max']))


#среднее значение количества населения по регионам
print('среднее значение количества населения по регионам')
temp1=round(df.groupby(by = 'Region')['Population'].mean())
print(temp1)
#круговая диаграмма
temp1.plot(kind = 'pie')

#сумарная площадь  по регионам
print('Cуммарная площадь')
temp2=round(df.groupby(by = 'Region')['Area (sq. mi.)'].sum())
print(temp2)
#круговая диаграмма
temp2.plot(kind = 'pie')


#сводная таблица
#temp = df.pivot_table(index = 'GDP ($ per capita)', columns = 'Literacy (%)', values = 'Summa', aggfunc ='mean')
#print(temp)

# диаграмма
temp.plot(kind = 'barh', grid = True)

plt.show()

