import matplotlib.pyplot as plt
import numpy as np

# Months and pollutant data (approximate values based on the chart)
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

PM10 = [135.82, 133.23, 130.77, 118.63, 110.11, 82.04, 61.97, 67.54, 79.41, 116.04, 156.80, 136.47]
PM25 = [58.02, 50.97, 46.34, 43.87, 36.35, 25.33, 22.66, 25.86, 29.04, 47.27, 73.68, 64.20]
SO2 = [14.16, 14.78, 14.32, 15.53, 13.73, 12.18, 11.36, 11.57, 11.50, 12.44, 13.91, 13.37]
NO2 = [60.70, 66.64, 60.85, 52.41, 48.99, 36.41, 32.84, 33.36, 38.86, 60.38, 91.96, 78.94]
Ozone = [42.46, 45.11, 45.78, 50.82, 58.04, 49.23, 33.29, 27.56, 30.40, 38.53, 45.80, 46.70]

plt.figure(figsize=(11,6))
plt.plot(months, PM10, marker='o', label='PM10', color='#17becf')
plt.plot(months, PM25, marker='o', label='PM2.5', color='#ffbb78')

plt.plot(months, SO2, marker='o', label='SO2', color='#8c564b')
plt.plot(months, NO2, marker='o', label='NO2', color='#bab0ac')
plt.plot(months, Ozone, marker='o', label='O3', color='#bcbd22')

plt.title('Chhoti Gwaltoli, Indore - Avg. Monthly Pollutant Conc. (2020-2024)', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Conc. (µg/m³)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
