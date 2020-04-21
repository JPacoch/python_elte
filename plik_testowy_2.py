import matplotlib.pyplot as plt
import xlrd as x
import pandas as pd

fortune500 = pd.read_csv('C:/Users/Jakub/Downloads/fortune500_2017.csv', delimiter=';')
fortune500.columns = ['rank', 'company', 'sector', 'revenue', 'profit', 'employees']
fortune50 = fortune500.head(50)
print(fortune50)
fortune50.sort_values(by = 'profit').plot(kind = 'barh', x = 'company', y = 'profit', figsize = [10,10])
plt.show()

