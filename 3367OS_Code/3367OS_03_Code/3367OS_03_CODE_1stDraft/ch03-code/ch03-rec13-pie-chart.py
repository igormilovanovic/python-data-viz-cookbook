import matplotlib.pyplot as plt

# make a square figure and axes
# pie chart looks best in square figures
# otherwise it looks like ellipses
plt.figure(1, figsize=(8, 8))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Spring', 'Summer', 'Autumn', 'Winter'
values = [15, 16, 16, 28]
explode =[0.1, 0.1, 0.1, 0.1]

# make a pie 
plt.pie(values, explode=explode, labels=labels,
    autopct='%1.1f%%', startangle=67)

plt.title('Rainy days by season')

plt.show()
