# %%
import pandas as pd
# %%
df = pd.read_csv('data/points_tmw.csv', sep=',')
df.head()
# %%
freq = pd.DataFrame(df['descProduto'].value_counts()
                                     .sort_index()
                    )
                    
freq['Freq Abs Acum'] = freq['count'].cumsum()
freq['Freq Relat (%)'] = (freq['count'] / freq['count'].sum()) * 100
freq['Freq Relat Acum (%)'] = freq['Freq Relat (%)'].cumsum()
freq
# %%


# %%
