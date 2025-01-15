import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

education_districtwise = pd.read_csv('education_districtwise.csv')
#removes missing values in the csv
education_districtwise = education_districtwise.dropna()


#Plot a histogram and display it
education_districtwise['OVERALL_LI'].hist()


#Find the average and stdev of the overall Literacy
mean_overall_li = education_districtwise['OVERALL_LI'].mean()
print(mean_overall_li)

std_overall_li = education_districtwise['OVERALL_LI'].std()
print(std_overall_li)

#Find the lower and upper limit of the normal distribution within one sd
lower_limit = mean_overall_li - 1 * std_overall_li
upper_limit = mean_overall_li + 1 * std_overall_li

one_sd = ((education_districtwise['OVERALL_LI'] >= lower_limit) & (education_districtwise['OVERALL_LI'] <= upper_limit)).mean()
print(one_sd)

#Add a new column that displays the district's zscores

education_districtwise['Z_Score'] = stats.zscore(education_districtwise['OVERALL_LI'])

#Filter out Zscores that are below -3 or above 3


filtered_ZScores = education_districtwise[(education_districtwise['Z_Score'] > 3) | (education_districtwise['Z_Score'] < -3)]
print(filtered_ZScores)