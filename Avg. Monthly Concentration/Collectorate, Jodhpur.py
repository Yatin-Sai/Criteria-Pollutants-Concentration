import matplotlib.pyplot as plt
import numpy as np

# Months and pollutant data (approximate values based on the chart)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

pm10 = [141.91, 167.39, 136.84, 116.02, 148.27, 115.89, 111.22, 96.10, 84.18, 122.23, 201.75, 164.77]
pm25 = [69.05, 81.13, 66.02, 55.97, 75.76, 54.77, 51.24, 44.91, 39.01, 54.44, 91.89, 72.77]
so2 = [7.96, 8.55, 9.11, 6.63, 7.18, 8.96, 7.59, 9.09, 8.65, 7.50, 7.59, 7.85]
no2 = [29.34, 25.41, 36.26, 25.77, 22.97, 21.43, 19.54, 18.96, 16.40, 36.05, 49.49, 32.57]
ozone = [34.19, 37.31, 38.74, 36.70, 44.58, 53.18, 29.41, 25.03, 22.19, 28.68, 32.93, 28.22]


plt.figure(figsize=(11,6))
plt.plot(months, pm10, marker='o', label='PM10', color='#17becf')
plt.plot(months, pm25, marker='o', label='PM2.5', color='#ffbb78')

plt.plot(months, so2, marker='o', label='SO2', color='#8c564b')
plt.plot(months, no2, marker='o', label='NO2', color='#bab0ac')
plt.plot(months, o3, marker='o', label='O3', color='#bcbd22')

plt.title('Collectorate, Jodhpur - Avg. Monthly Pollutant Conc. (2020-2024)', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Conc. (µg/m³)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
