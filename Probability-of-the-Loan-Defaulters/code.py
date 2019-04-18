# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
# loading dataset
df = pd.read_csv(path)
total = len(df)

# calculating probability
p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print('Probability of fino credit score > 700 :',p_a)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/total
print('Probability of debt_consolidation :',p_b)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print('probaility of dept_consolidation given fino :',p_a_b)

# check for independency
result = p_a_b == p_a
print('Independancy :',result)
# code ends here


# --------------
# code starts here

# calculations using bayes theorem
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/total
print('Probability of loan paid back :',prob_lp)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/total
print('Probability of credit policy :',prob_cs)
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print('Probability of the Loan Defaulters :',bayes)



# code ends here


# --------------
# code starts here

# plotting bar graph
df.purpose.value_counts(normalize=True).plot(kind='bar')
df1 = df[df['paid.back.loan'] == 'No']
df1.purpose.value_counts(normalize=True).plot(kind='bar')
# code ends here


# --------------
# code starts here

# calculating median & mean
inst_median = df.installment.median()
print('Median of installment :',inst_median)
inst_mean = df.installment.mean()
print('Mean of installment :',inst_mean)

# plotting histogram
plt.hist(df.installment)
plt.hist(df['log.annual.inc'])
# code ends here


