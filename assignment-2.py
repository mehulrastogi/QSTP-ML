import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib
# import seaborn as sns


data = pd.read_csv('../homicide_database.csv')
data.head()

# TASK 1
# Show how the usage of a given weapon varied.
# Plot frequency of a weapon used vs year(simple line plot preferably). 


for x in data['Weapon'].unique():
    weapon = data[data['Weapon'] == x]
    cnt = np.array(weapon['Year'].value_counts(sort = False))

    # print sorted(handgun["Year"].unique())
    plt.xlabel('Year')
    plt.ylabel('Frequency of Weapon')#(No. of lives cliamed by this weapon)
    plt.title('{}---Year V/s Frequency'.format(x))

    plt.plot(sorted(weapon["Year"].unique()), cnt )
    plt.show()

# Spike in use of all types of firearms between the year 1990-1995
# this may be due to either change of law regarding firearms in the usa
# or drop in their prices

# IN EXPLOSIVES SPIKE IN THE YEAR 1995 DUE TO OKHLOHOMA STATE BOMBINGS






# TASK 2 --- 
# For a given relationship how the number of homicides has varied with time


for x in data['Relationship'].unique():
    rela = data[data['Relationship'] == x]
    cnt = np.array(rela['Year'].value_counts(sort = False))

    # print sorted(handgun["Year"].unique())
    plt.xlabel('Year')
    plt.ylabel('Frequency of realationship')#(No. of lives 
    plt.title('{}---Year V/s Frequency'.format(x))

    plt.plot(sorted(rela["Year"].unique()), cnt )
    plt.show()

# TASK 3
# A Box plot of weapon Vs year

plt.figure(0)
data.boxplot(column='Year' , by ='Weapon' , rot = 90, fontsize = 15)
plt.show()




