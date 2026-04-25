import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([10,20,30,40,50,68,70,80,90,100])
print(s)
print("Head",s.head())
print("Tail",s.tail())
print("add 5 \n",s+5)
print("mul 2 \n",s*2)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'marks': [25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)
print(df)
for index, row in df.iterrows():
    print(f"Name: {row['Name']}, Marks: {row['marks']}")
print(df['marks'])
df['grade'] = ['A', 'B', 'C', 'D', 'E']
print(df)
df.drop('grade', axis=1, inplace=True)
print(df)
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
print("adding two dataframes \n",df1 + df2)
print("multiplying two dataframes \n",df1 * df2)
print("subtracting two dataframes \n",df1 - df2)
print("dividing two dataframes \n",df1 / df2)
df = pd.DataFrame(({'A': [1, 2, 3], 'B': [4, 5, 6]}))
print(df+10)
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [4, 5, 6]
})
print("original dataframe \n",df)
df1 = df.fillna(0)
print("after filling NaN with 0 \n",df1)
df2 = df.fillna(df.mean())
print("after filling NaN with mean \n",df2)
df3 = df.dropna()
print("after dropping rows with NaN \n",df3)
df4= df.fillna(method='ffill')
print("after filling NaN with forward fill \n",df4)
df5 = df.fillna(method='bfill')
print("after filling NaN with backward fill \n",df5)
