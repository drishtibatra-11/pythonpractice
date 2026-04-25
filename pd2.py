using pandas as pd
import numpy as np
df = pd.DataFrame({
    'A': [1, 2, 4, 4, 5],
    'B': [4, 5, 6, 7, 8]
})
print("sum of columns \n",df.sum())
print("mean of columns \n",df.mean())
print("max of columns \n",df.max())
print("min of columns \n",df.min())
df = pd.DataFrame({
    'A': [1, 2, 4, 4, 5]})
    print(df > 1)
    df = pd.DataFrame({
    'A': [True, False, True, False, True]})
print(df.any())
print("all values are True?", df.all())
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([5, 4, 3, 2, 1])
print(s1 == s2)
