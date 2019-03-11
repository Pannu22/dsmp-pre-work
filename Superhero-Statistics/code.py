# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace = True)
gender_count = data.Gender.value_counts()
plt.bar(gender_count.index, gender_count)
plt.show()



# --------------
#Code starts here
alignment = data.Alignment.value_counts()
plt.pie(alignment)
plt.title('Character Alignment')


# --------------
#Code starts here

#Create a subset having columns Strength & Combat
sc_df = data.loc[ : , ['Strength', 'Combat']]

#Calculating Covariance between Strength & Combat
sc_covariance  = round((sc_df.cov().values[0, 1]), 2)
print('Covariance between Strength & Combat :', sc_covariance)

#Calculating standard deviation of Strength & Combat
sc_strength = round((sc_df.Strength.std()), 2)
print('Standard deviation of Strength :', sc_strength)
sc_combat = round((sc_df.Combat.std()), 2)
print('Standard devition of Combat :', sc_combat)

#Calculating pearson's correlation coefficient between Strength & Combat
sc_pearson = round(((sc_covariance) / (sc_combat * sc_strength)), 2)
print('Pearsons correlation coefficient between Strength & Combat :', sc_pearson)

#Create a subset having columns Intelligence & Combat
ic_df = data.loc[: , ['Intelligence', 'Combat']]

#Calculating Covariance between Intelligence & Combat
ic_covariance  = round((ic_df.cov().values[0, 1]), 2)
print('Covariance between Intelligence & Combat :', ic_covariance)

#Calculating standard deviation of Intelligence & Combat
ic_intelligence = round((ic_df.Intelligence.std()), 2)
print('Standard deviation of Intelligence :', ic_intelligence)
ic_combat = round((ic_df.Combat.std()), 2)
print('Standard devition of Combat :', ic_combat)

#Calculating pearson's correlation coefficient between Intelligence & Combat
ic_pearson = round(((ic_covariance) / (ic_combat * ic_intelligence)), 2)
print('Pearsons correlation coefficient between Intelligence & Combat :', ic_pearson)







# --------------
#Code starts here

#Calculation for column Total for the value of quantile=0.99
total_high = data.Total.quantile(0.99)
print('Quantile :', total_high)

#Creating subset of Super Beings
super_best = data[data.Total > total_high]
print('Super Best :', super_best)

#Getting list of Nmaes of Super Beings
super_best_names = [super_best.Name]
print('Super Names :', super_best_names)


# --------------
#Code starts here

#Created subplots with axes
fig = plt.figure()
ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)

#Plotted boxplots
ax_1.boxplot(data.Intelligence)
ax_1.set_title('Intelligence')
ax_2.boxplot(data.Speed)
ax_2.set_title('Speed')
ax_3.boxplot(data.Power)
ax_3.set_title('Power')



