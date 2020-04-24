import matplotlib.pyplot as plt
import xlrd as x
import pandas as pd

fortune500 = pd.read_csv('C:/Users/Jakub/Downloads/fortune500_2017.csv', delimiter=';')
fortune500.columns = ['rank', 'company', 'sector', 'revenue', 'profit', 'employees']
fortune50 = fortune500.head(50)
#print(fortune50)
#fortune50.sort_values(by = 'profit').plot(kind = 'barh', x = 'company', y = 'profit', figsize = [10,10])
#plt.show()

df = pd.read_csv('C:/Users/Jakub/Downloads/airports.csv', delimiter=';')

df_sort = df.sort_values(by = 'longest', ascending=False)
df_100 = df_sort.head(100)
print(df_100)

#df_100.plot(kind = 'bar', x = 'iata', y = 'longest', figsize = [20,3])
#plt.show()

df_sort_city = df_sort.groupby('city')['longest'].max()
df_sort_city1 = df_sort_city.sort_values(ascending=False)
df_100_city = df_sort_city1.head(100)
df_100_city.columns = ['city', 'longest']

#df_100_city.plot(kind = 'bar', x = 'city', y = 'longest', figsize = [20,3])
#plt.show()

df_count = df.groupby('country').count()
df_count_sorted = df_count.sort_values(by = 'iata', ascending=False)

df_elev = df.groupby('city')['elevation'].mean()
df_elev_sorted = df_elev.sort_values(ascending=False)

