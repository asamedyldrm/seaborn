import seaborn as sns

planets = sns.load_dataset("planets")
df = planets.copy()
print(df.head())

# hic eksik gozlem var mi?

print(df.isnull().values.any())  # True oldugu icin eksik gozlem var.

# hangi degiskende kacar tane eksik var?

print(df.isnull().sum())

df["orbital_period"].fillna(0, inplace=True)  # eksik degerlerin hepsi sifir olmus oldu.
print(df.isnull().sum())

df["mass"].fillna(df.mass.mean(), inplace=True)  # mass'deki eksik degerlerin yerine ortalamasi geldi.
print(df.isnull().sum())

# df.fillna(df.mean(),inplace=True) #veri setindeki tum eksik degerlerin yerine ortalama degerler atanir.
print(df.isnull().sum())

df = planets.copy()
print(df.head())
print(df.isnull().sum())
