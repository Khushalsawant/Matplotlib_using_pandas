# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:17:57 2019

@author: khushal
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
ax=plt.gca()

pd.set_option('display.max_columns',1000)
path_of_input_file = "C:/Users/khushal/Documents/Python Scripts/Rape_cases_in_India_2015.xlsx"
input_data_df = pd.read_excel(path_of_input_file,sheet_name='Rape_cases_in_India_2015')
indian_states_df = pd.read_excel(path_of_input_file,sheet_name='States')
input_data_df.sort_values(by='Number of Victims (Total Rape Cases) - Total Victims')

print(input_data_df)

print("--" * 60)
india_crime_data_by_state = pd.merge(left=input_data_df,right=indian_states_df,left_on='State/UT',right_on='State/UT')
state_df = india_crime_data_by_state['State/UT']

#incest_rape_case_reported_df = input_data_df['Incest Rape - Number of Cases Reported']
Number_of_Victims_under_Incest_Rape_Cases = india_crime_data_by_state['Number of Victims under Incest Rape Cases - Total Victims']
Number_of_Victims_under_Other_than_Incest_Rape_Cases = india_crime_data_by_state['Number of Victims under Other than Incest Rape Cases - Total Victims']
Number_of_Victims_Total_Rape_Cases_Total_Victims = india_crime_data_by_state['Number of Victims (Total Rape Cases) - Total Victims']

#print("india_crime_data_by_state = \n",india_crime_data_by_state,"\n --" * 60)
#print(Number_of_Victims_Total_Rape_Cases_Total_Victims)

input_data_df.plot(kind='bar',x='State/UT',y='Number of Victims (Total Rape Cases) - Total Victims',label='Rape_cases_in_India_2015')
plt.show()