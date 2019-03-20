import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(s)
print(dates)
print(df)
print(df2)
print(df2.dtypes)
print(df.head())
print(df.tail(3))
print(df.columns)

print(df.to_numpy())
print(df2.to_numpy())

print("\n")
print(df.describe())
print("\n")
print(df.T)

ts = pd.Series(np.random.randn(1000),
                index=pd.date_range('1/1/2000', periods=1000))


ts = ts.cumsum()

ts.plot()
plt.savefig('images/test-foo.png')
