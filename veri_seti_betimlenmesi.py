import seaborn as sns

planets = sns.load_dataset("planets")
df = planets.copy()
print(df.head())

print(df.shape)
print(df.columns)
print(df.describe()) #eksik gozlemleri gozardi eder, kategorik degiskenleri disarida birakir.
print(df.describe(include="all").T)

