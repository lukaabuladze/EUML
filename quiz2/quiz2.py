import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
excel_file = 'quiz3_data.xlsx'
people = pd.read_excel(excel_file)
#დავალება 1
ageGender =  people.groupby("Gender")["Age"].mean()
print("საშუალო წლოვანება", ageGender)
#დავაკება 2
count_Cou = people["Country"].value_counts()
print("ქვეყნები")
print(count_Cou)
#დავალება3
people["Age"].plot()
#დავალება 4
countr_Age = people.groupby("Country")["Age"].mean()
print(min(countr_Age))

