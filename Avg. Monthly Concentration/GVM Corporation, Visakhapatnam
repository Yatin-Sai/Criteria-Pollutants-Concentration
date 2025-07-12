import matplotlib.pyplot as plt
import numpy as np

# Months and pollutant data (approximate values based on the chart)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

PM10 = [156.7, 131.8, 110.5, 99.1, 94.5, 97.9, 98.1, 96.4, 98.7, 112.6, 122.1, 120.7]
PM25 = [85.9, 66.5, 51.8, 36.7, 32.5, 31.8, 31.0, 29.1, 32.6, 42.7, 54.6, 55.3]
SO2 = [10.8, 10.3, 10.3, 10.9, 10.8, 10.2, 9.7, 9.7, 9.5, 9.0, 9.1, 9.3]
NO2 = [39.6, 36.8, 33.7, 34.1, 32.3, 34.9, 37.8, 36.7, 37.2, 41.2, 44.0, 43.9]
Ozone = [21.2, 19.5, 17.1, 17.7, 18.3, 13.7, 13.6, 12.2, 13.9, 16.2, 17.6, 18.0]

plt.figure(figsize=(11,6))
plt.plot(months, PM10, marker='o', label='PM10', color='#17becf')
plt.plot(months, PM25, marker='o', label='PM2.5', color='#ffbb78')

plt.plot(months, SO2, marker='o', label='SO2', color='#8c564b')
plt.plot(months, NO2, marker='o', label='NO2', color='#bab0ac')
plt.plot(months, Ozone, marker='o', label='O3', color='#bcbd22')

plt.title('GVM Corporation,Visakhapatnam - Avg. Monthly Pollutant Conc. (2020-2024)', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Conc. (µg/m³)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
