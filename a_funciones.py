import pandas as pd
from sklearn.impute import SimpleImputer

### Función para conocer información de cada una de las variables del dataframe
def info_columns(df):
    for i in df.columns:
        print(i, df[i].unique())
    print("Tamaño del DataFrame:",df.shape)


#Función que imputa datos para variables numéricas
def impute_columns(df, columns, strategy): 
  imputer = SimpleImputer(strategy=strategy)
  for column in columns:
    column_imputed = imputer.fit_transform(df[column].values.reshape(-1, 1))
    df[column] = column_imputed.flatten()
  return df