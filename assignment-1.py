import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

data = pd.read_csv('./homicide_database.csv')
data.head()

#Task -1
# Number of Crimes Solved
cnt = data[data['Crime Solved']== 'Yes'].count()[0]
print("The number of solved crimes are: ", cnt)

data['Crime Solved'].value_counts().plot(kind = 'bar')
plt.show()

#Task 2
# Top 5 Weapons used
data_weapon = data[data['Weapon'] != 'Unknown']	
print(" \nThe Weapons List is:")	
print (data_weapon['Weapon'].value_counts())
data_weapon['Weapon'].value_counts().plot(kind = 'bar')
plt.show()

'''
Handgun          317484
Knife             94962
Blunt Object      67337
Firearm           46980
Shotgun           30722
'''


#Task 3
#Top Weapon in each state with its percentage there
# count of weapon in state / total weapons in sate
print ("\n\n\nState wise top three are:")

states = data_weapon.State.unique()
for x in states:
   
    try:
        plot  = data_weapon[data_weapon['State']==x]
        count= int(plot.count()[0])	
        #creating a list with frequency of weapons and then sorting it 
        s = plot[['Weapon','Record ID']].groupby('Weapon')['Record ID']\
                .count().reset_index(name = 'count')\
                .sort_values(['count'],ascending = False)
        
        print ("\n\n",x)
        print (" \nThe Percentage of top three Weapon Used in ",x," are:-")
        
        for i in range(0,3):
            print (s.iloc[i,0] , " : " , (float(s.iloc[i,1]) / count) * 100)
        
        ax = plt.axes()
        sns.barplot(x = 'Weapon',y = 'count', data = s,ax=ax)
        plt.xticks(rotation =90)
        ax.set_title(x)
        plt.show()

    except(ValueError):
        pass
  


#Task 4
#Bar plot of homicide v/s year
sns.countplot(data=data,x = 'Year')
plt.xticks(rotation =90)			#to rotate labels on x axis
plt.show()

