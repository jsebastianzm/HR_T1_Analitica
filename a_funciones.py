import pandas as pd

### Función para conocer información de cada una de las variables del dataframe
def info_columns(df):
    for i in df.columns:
        print(i, df[i].unique())
    print("Tamaño del DataFrame:",df.shape)
