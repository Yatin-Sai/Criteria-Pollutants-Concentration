import matplotlib.pyplot as plt
import numpy as np

# Months and pollutant data (approximate values based on the chart)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

pm10 = [371.83, 326.35, 249.34, 240.14, 226.16, 211.84, 119.80, 173.27, 176.61, 377.78, 482.93, 387.39]
pm25 = [225.52, 143.55, 94.86, 91.70, 86.01, 71.69, 45.87, 48.83, 57.55, 132.28, 260.51, 234.25]
so2 = [16.26, 17.48, 23.68, 24.28, 17.82, 14.32, 13.80, 13.28, 14.36, 16.90, 16.91, 14.94]
no2 = [74.52, 87.96, 69.29, 84.71, 74.42, 63.13, 53.57, 48.28, 45.84, 79.04, 104.90, 100.47]
o3 = [21.86, 24.31, 33.94, 46.37, 51.67, 45.47, 45.90, 38.32, 34.78, 31.15, 23.28, 15.12]

plt.figure(figsize=(11,6))
plt.plot(months, pm10, marker='o', label='PM10', color='#17becf')
plt.plot(months, pm25, marker='o', label='PM2.5', color='#ffbb78')

plt.plot(months, so2, marker='o', label='SO2', color='#8c564b')
plt.plot(months, no2, marker='o', label='NO2', color='#bab0ac')
plt.plot(months, o3, marker='o', label='O3', color='#bcbd22')

plt.title('Anand Vihar, Delhi - Avg. Monthly Pollutant Conc. (2020-2024)', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Conc. (µg/m³)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
