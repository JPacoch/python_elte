import geopandas as gpd
import matplotlib.pyplot as plt

countries = gpd.read_file('datasets/ne_10m_admin_0_countries.shp')
#print(countries)

countries.plot(figsize=[20,10])
plt.show()
