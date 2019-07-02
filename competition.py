# This is my first time participating in a machine learning competition and actually
#  getting my hands dirty with data science!
# The objective is to automate a company's home loan eligibility process (real time)
#  based on customer detail provided while filling an online application form.
#  These details are Gender, Marital, Status, Education, Number of Dependents, Income,
#  Loan Amount, Credit History and others.

# More information on the link down below:
# https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/

# Some tips:
# https://www.analyticsvidhya.com/blog/2016/01/guide-data-exploration/

print('Import necessary libraries')
import pandas as pd
import numpy as np
import matplotlib as plt
#import scikit-learn as sc


# Open and store the train data frame
train_df = pd.read_csv('train_ctrUa4K.csv')
# Need to put it in a development environment
train_df.head(10)
#print(train_df)
