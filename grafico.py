# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
# %%
df = pd.read_csv('data/points_tmw.csv')
df
# %%
group_prod = (df.groupby('descProduto')
          .agg({'qtdPontos':'sum','idTransacao':'count'})
          .reset_index()
          .sort_values('idTransacao')
          )

group_prod
# %%
sns.barplot(group_prod, x='idTransacao', y='descProduto')
plt.xlabel('Quantidade de transações')
plt.ylabel('Produtos')
plt.title('Frequência de produtos')
# %%
df['data_transacao'] = pd.to_datetime(df['dtTransacao']).dt.date

group_data = (df.groupby('data_transacao')
                .agg({'qtdPontos':'sum','idTransacao':'count'})
                .reset_index()
              )
group_data
# %%
sns.lineplot(group_data, x='data_transacao',y='idTransacao')
plt.title("Quantidade de operações diárias")
plt.xlabel('Data')
plt.ylabel('Quantidade de transações')
plt.show()
# %%
plt.hist(group_data['qtdPontos'], bins=20)
plt.show()
# %%
plt.boxplot(group_data['qtdPontos'])
plt.show()
# %%
