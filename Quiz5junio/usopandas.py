import pandas as pd
import numpy as np


#cada "n" es un elemento pseudoaleatorio
data = {"n": np.random.randint(1,100, 100)}
# se crea un dataframe en data
df = pd.DataFrame(data)
print(df.head())

# se asigna a qs la funcion cuantiles evaluando el 25, 50 y 75 %
qs = df.n.quantile([.25, .50, .75]).values

#para cada df se creara una columna a la que se asignara el valor despues del =
df["Q1"] = (df.n <=qs[0])+0
df["Q2"] = ((df.n <=qs[1]) & (df.n >qs[0])) +0
df["Q3"] = ((df.n <=qs[2]) & (df.n >qs[1])) +0
df["Q4"] = (df.n >qs[2]) +0

print(df.head())

