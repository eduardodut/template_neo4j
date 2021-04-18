# %% Import e inicialização da conexão
from neo4j import GraphDatabase
import nxneo4j as nx
import wget, os
import pandas as pd
import numpy as np

driver = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","test"))
G = nx.Graph(driver)

# %% Primeiros testes
G.delete_all()
G.add_node(1)                   #single node
G.add_nodes_from([2,3,4])       #multiple nodes
G.add_edge(1,2)                 #single edge
G.add_edges_from([(2,3),(3,4)]) #multiple edges
G.add_node('Mike',gender='M',age=17)
G.add_edge('Mike','Jenny',type='friends',weight=3)
nx.draw(G)

# %% Deleta os dados existentes e insere os novos dados
G.delete_all()
colaboracao = pd.read_csv('dados\collaboration.edgelist.txt',delimiter='\t',header=None)

lista_df = np.array_split(colaboracao,20)

# %%
for resultado in lista_df:
    records = resultado.to_records(index=False)
    results = [(int(tupla[0]),int(tupla[1])) for tupla in list(records)]
    G.add_edges_from(results) 

# %% Formatação dos nós e relações

def renomear_nodes(tx):
    tx.run("match (n:Node) set n:Pesquisador remove n:Node")
def renomear_relacoes(tx):
    tx.run("match p=(a:Pesquisador)-[r:CONNECTED]-(b:Pesquisador) merge (a)-[:COLABOROU_COM]-(b) delete r")
with driver.session() as session:
    session.write_transaction(renomear_nodes)
    session.write_transaction(renomear_relacoes)

# %%
