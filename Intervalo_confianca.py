# verificar valores onde o intervalo de confiança dos pontos agrupagos por 
# usuários, com 95% de probabilidade
# %%
import pandas as pd
from scipy.stats import t as t
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv('data/points_tmw.csv')
df.head()
# %%
# agrupar os pontos de cada usuário
pontos = df.groupby('idUsuario')[['qtdPontos']].sum().reset_index()
pontos
# %%
# função para obter a media amostral, desvio padrão amostral, limite inferior e superior 
# para uma amostra definida pelo usuário e com intervalo de confiança de 95%
def intervalo_confianca(sample, alpha=0.05):
    n = len(sample)
    x_barra = sample['qtdPontos'].mean()
    des_padrao = sample['qtdPontos'].std()
    variavel = t.ppf(1-alpha/2, n-1)
    inf = x_barra - variavel * des_padrao / np.sqrt(n)
    sup = x_barra + variavel * des_padrao / np.sqrt(n)
    return x_barra, des_padrao, inf, sup
# %%
# gera dos dados a partir de uma amostra de 100 usuários aleatórios, gerando dados 1000 vezes
status = []
for i in range(1000):
    n=100
    sample = pontos.sample(n)
    status.append(intervalo_confianca(sample))

int_conf = pd.DataFrame(status, columns=['x_barra','desvio_padrao','inf','sup'])
int_conf['media_pop'] = pontos['qtdPontos'].mean()
int_conf['check'] = (int_conf['media_pop'] > int_conf['inf']) & (int_conf['media_pop'] < int_conf['sup'])
int_conf
# %%
# Verifica qual o nível de confiança o código acima conseguiu. Se a média populacional ficou dentro
# do intervalo de confiança calculado para cada amostra. Se igual ou próximo de 0.95, é por que
# o modelo está funcionando
int_conf['check'].mean()
# %%
# cria o gráfico onde mostra visualmente os samples que estão dentro ou fora do intervalo de confiança
for i in range(100):
    data = int_conf.iloc[i]
    color = 'green' if data['check'] else 'red'
    plt.plot(data[['inf','sup']], [i,i],'x-', color=color)
plt.vlines(int_conf['media_pop'].max(), -1,i+1)
plt.title('Gráfico de intervalos de confiança')
plt.xlabel('Valor esperado')
plt.ylabel("Amostra")
# %%
for i in range(100):
    data = int_conf.iloc[i]
    inf = data['inf']
    sup = data['sup']
    color = 'green' if data['check'] else 'red'
    plt.hlines(y=i, xmin=inf, xmax=sup, linestyles='solid', colors=color)
plt.vlines(int_conf['media_pop'].max(), -1,i+1)
plt.title('Gráfico de intervalos de confiança')
plt.xlabel('Valor esperado')
plt.ylabel("Amostra")
# %%
