import matplotlib.pyplot as plt
import numpy as np

# Months and pollutant data (approximate values based on the chart)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

PM10 = [264.4, 239.7, 170.6, 190.7, 164.9, 116.7, 77.0, 70.7, 85.5, 126.6, 232.8, 201.3]
PM25 = [132.2, 108.9, 72.1, 82.2, 73.3, 54.3, 34.2, 31.1, 39.7, 57.8, 111.6, 98.6]
SO2 = [13.5, 13.4, 9.8, 8.6, 7.9, 6.5, 6.5, 7.0, 7.1, 7.7, 8.7, 8.1]
NO2 = [54.6, 61.6, 27.7, 21.3, 19.3, 14.8, 13.7, 15.6, 23.4, 34.2, 51.0, 43.7]
Ozone = [17.0, 22.5, 34.7, 44.1, 48.2, 38.3, 22.9, 13.2, 14.7, 18.1, 18.4, 22.8]


plt.figure(figsize=(11,6))
plt.plot(months, PM10, marker='o', label='PM10', color='#17becf')
plt.plot(months, PM25, marker='o', label='PM2.5', color='#ffbb78')

plt.plot(months, SO2, marker='o', label='SO2', color='#8c564b')
plt.plot(months, NO2, marker='o', label='NO2', color='#bab0ac')
plt.plot(months, Ozone, marker='o', label='O3', color='#bcbd22')

plt.title('Rajbansi Nagar, Patna - Avg. Monthly Pollutant Conc. (2020-2024)', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Conc. (µg/m³)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
