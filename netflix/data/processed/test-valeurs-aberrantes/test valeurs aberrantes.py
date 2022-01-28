import pandas as pds
import numpy as np

LigneAberantes = []
df = pds.read_csv("merged.csv")
LigneAberantes = (sum(df.loc[:, df.colums == 'merged.csv'].isnull.values.ravel() + LigneAberantes))
print( LigneAberantes )

LigneAberantes = float(0)


