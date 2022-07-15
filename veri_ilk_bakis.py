# Veri Gorsellestirme Alaninda Kullanilan Kutuphaneler

# - Matplotlib
# - Pandas
# - Seaborn
# - ggplot
# - Bokeh
# - Plot.ly

# Veri Ilk Bakis

# veri sati hikayesi ve yapisinin incelenmesi
import seaborn as sns

planets = sns.load_dataset("planets")

# veri setinin hikayesi nedir?

# once yedegini alalim.

df = planets.copy()
print(df.head())

print("-----veri seti yapisal bilgileri-----")
df.info()

# object : kategorik degisken (str)

print(df.dtypes)

import pandas as pd
df.method = pd.Categorical(df.method)
print(df.dtypes)
print(df.head())