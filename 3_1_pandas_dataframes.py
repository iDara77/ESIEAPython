import pandas as pd

grid = [[1,2,3], [4,5,6], [7,8,9]]
print("Python")
print(grid)
print("Pandas no headers")
df = pd.DataFrame(grid)
print(df)
print("Pandas with headers")
df = pd.DataFrame(grid, columns=["one", "two", "three"] )
print(df)
print(df["two"])
print("Pandas edges")
edges = df[["one", "three"]]
print(edges)
print("Pandas quick op - add")
print(edges.add(2))