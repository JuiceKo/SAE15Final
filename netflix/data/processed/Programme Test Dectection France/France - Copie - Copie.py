import pandas as pd

x = 0
df = pd.read_csv("merged.csv")
a = df.iloc[:, [5]]
for i in df["country"]:
    if "France" in str(i) and df["type" [i]]:
        print(i)
        x = x + 1
print("Il y a", x, "films français")