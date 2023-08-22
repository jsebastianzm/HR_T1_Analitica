# -*- coding: utf-8 -*-
"""Taller 1 Analitica 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1reJOJ6SrVhOHEtANhsh2Iu4vD3KgO2_6

#Librerias
"""

import numpy as np
import matplotlib as mp
import pandas as pd

"""#Bases de datos"""

data_employee = pd.read_csv("employee_survey_data.csv")
data_general = pd.read_csv("general_data.csv",sep=";")
data_manager_survey = pd.read_csv("manager_survey_data.csv")
data_retirement = pd.read_csv("retirement_info.csv",sep=";")

# data_employee.head()
# data_general.head()
# data_manager_survey.head()
# data_retirement.head()

"""# General Data

"""

data_general.head()

for i in data_general.columns:
  print(i, data_general[i].unique())
print(data_general.shape)

"""Se puede eliminar las columnas: -EmployeeCount, ya que tiene solo 1 valor.
                                -Over18, ya que todos son mayores de 18.
                                -StandardHour, ya que las horas estandares son  8 para todos.

Se deben tratar los datos nulos: -NumCompaniesWorked, se puede remplazar los
                                     nan por la moda.
                                 -TotalWorkingYears, Tambien se puede cambiar
                                     por la moda.

"""

data_general = data_general.drop(columns=['EmployeeCount','Over18', 'StandardHours'])

print(data_general.columns, data_general.shape)

data_general.info()

"""#Employee Data

"""

data_employee.head()

for i in data_employee.columns:
  print(i, data_employee[i].unique())
print(data_employee.shape)

"""Se debe analizar la variable

#Manager Data
"""

data_manager_survey.head()

for i in data_manager_survey.columns:
  print(i, data_manager_survey[i].unique())
print(data_manager_survey.shape)

"""#Retirement Data"""

data_retirement.head()

for i in data_retirement.columns:
  print(i, data_retirement[i].unique())
print(data_retirement.shape)