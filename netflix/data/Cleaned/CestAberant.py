import pandas as pds

def ComputeMean():
    mean = 0
    df=pds.read_csv("merged.csv")
    x=df.iloc[:,1]
print(x.mean)
    
