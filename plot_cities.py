# %%
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# %%
cities = [["Chicago",42, -87],
          ["Boston", 42, -71],
          ["New York", 41, -74],
          ["Seattle", 48, -122],
          ["San Francisco", 37, -122],]
scale = 5

# %%
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=30,lat_2=45,lon_0=-95)

map.drawcoastlines()
map.drawcountries()
map.drawstates()


watercolor = "lightskyblue"
map.fillcontinents(color='seagreen',lake_color=watercolor)
map.drawmapboundary(fill_color=watercolor)
map.drawparallels(range(20, 60, 10), labels=[1,0,0,0])
map.drawmeridians(range(-120, -60, 20), labels=[0,0,0,1])
map.etopo(scale=0.5, alpha=0.5)

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
plt.show()

# %%
