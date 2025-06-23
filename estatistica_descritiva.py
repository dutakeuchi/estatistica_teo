# %% 
import pandas as pd
# %%
df = pd.read_csv('data/points_tmw.csv')
df.head()
# %%
media = df['qtdPontos'].mean()
print('Média :',media)

minimo = df['qtdPontos'].min()
print('Mínimo :',minimo)

quartil_1 = df['qtdPontos'].quantile(q=0.25)
print('1º quartil :',quartil_1)

mediana = df['qtdPontos'].quantile(q=0.5)
print('Mediana :',mediana)

quartil_3 = df['qtdPontos'].quantile(q=0.75)
print('3º quartil :',quartil_3)

maximo = df['qtdPontos'].max()
print('Máximo :',maximo)

variancia = round(df['qtdPontos'].var(),5)
print('Variancia :',variancia)

desvio_padrao = round(df['qtdPontos'].std(),5)
print('Desvio Padrao :',desvio_padrao)
# %%
df["qtdPontos"].describe()
# %%
usuarios = df.groupby(['idUsuario']).agg({'idTransacao':'count', 'qtdPontos':'sum'}).reset_index()
usuarios
# %%
usuarios[['idTransacao','qtdPontos']].describe()
# %%
usuarios
# %%
