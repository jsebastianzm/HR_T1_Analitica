# -*- coding: utf-8 -*-
"""Taller 1 Analitica 3
#Librerias
"""
import numpy as np
import matplotlib as mp
import pandas as pd
import sqlite3 as sql #### para bases de datos sql
import sys ## saber ruta de la que carga paquetes
import a_funciones as fn

# """Ruta directorio qué tiene paquetes"""
# sys.path
# sys.path.append('C:\codigos\HR_T1_Analitica')

"""#Bases de datos"""

employee = 'data/employee_survey_data.csv'
general = 'data/general_data.csv'
manager_survey = 'data/manager_survey_data.csv'
retirement = 'data/retirement_info.csv'


data_employee = pd.read_csv(employee)
data_general = pd.read_csv(general ,sep=";")
data_manager_survey = pd.read_csv(manager_survey)
data_retirement = pd.read_csv(retirement ,sep=";")


"""# General Data"""

data_general.head()# Observar la base de datos general
fn.info_columns(data_general) #Ver las columnas con sus respectivas variables con fin de buscar datos mal escritos
print(data_general.shape)

"""Se puede eliminar las columnas: -EmployeeCount, ya que tiene solo 1 valor.
                                -Over18, ya que todos son mayores de 18.
                                -StandardHour, ya que las horas estandares son  8 para todos.
                                StockOptionLevel: Probablemente tambien se puede eliminar ###

Se deben tratar los datos nulos: -NumCompaniesWorked, se puede remplazar los
                                     nan por la moda.
                                 -TotalWorkingYears, Tambien se puede cambiar
                                     por la moda.
                                  Pero antes de esto se tiene que evaluar la cantidad de datos nulos por columna

"""

data_general = data_general.drop(columns=['EmployeeCount','Over18', 'StandardHours']) # Se eliminan variables que no aporten
print(data_general.columns, data_general.shape) #Se evalua que se hayan eliminado las columnas anteriores
data_general.info() #Se observan el tipo de datos que se tiene y la cantidad de datos nulos

"""Se debe cambiar el tipo de las siguientes variables:

  DistanceFromHome: float64
  Education: object ("OneHotEncouder")
  EmployeeID: object
  Joblevel: object
  MonthlyIncome: float64
  NumCompaniesWorked: int64
  StockOptionLevel: object
  TotalWorkingYears: int64

"""

columns_object = ['Education', 'EmployeeID','JobLevel', 'StockOptionLevel']
columns_int = ['NumCompaniesWorked','TotalWorkingYears']
columns_float = ['DistanceFromHome','MonthlyIncome']
data_general[columns_object] = data_general[columns_object].astype(object)
data_general[columns_int] = data_general[columns_int].astype(int)
data_general[columns_float] = data_general[columns_float].astype(float)

data_general.info()

"""#Employee Data

"""

data_employee.head()


"""Se debe analizar la variable

#Manager Data
"""

data_manager_survey.head()


"""#Retirement Data"""

data_retirement.head()

