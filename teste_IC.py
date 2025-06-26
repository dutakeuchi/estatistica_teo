# %%
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t as t
# %%
df = pd.read_csv('data/points_tmw.csv')
df.head()
# %%
usuario = df.groupby('idUsuario')[['qtdPontos']].sum().reset_index()
usuario
# %%
def ic(sample, alpha=0.05):
    n=len(sample)
    media = sample.mean()
    desvio = sample.std()
    variavel = t.ppf(1-alpha/2, n-1) * desvio / n ** 0.5
    inf = media - variavel
    sup = media + variavel
    return (n, media, inf, sup)
# %%
lista = []
for i in range(1000):
    n = 100
    data = usuario['qtdPontos'].sample(n)
    data = ic(data)
    lista.append(data)

lista = pd.DataFrame(lista, columns=['amostra','media','inf','sup'])
lista['media_pop'] = usuario['qtdPontos'].mean()
lista['check'] = (lista['media_pop'] > lista['inf']) & (lista['media_pop'] < lista['sup'])
lista
# %%
n = 100
for i in range(n):
    data = lista.iloc[i]
    color = 'green' if data['check'] else 'red'
    plt.hlines(y=i, xmax=data['sup'], xmin=data['inf'], colors=color, linestyles='solid')
plt.vlines(x=data['media_pop'].mean(), ymin = -1, ymax = n+1, )

# %%
