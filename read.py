#%% Import e inicialização da conexão
from neo4j import GraphDatabase
import nxneo4j as nx
import wget, os
import pandas as pd
import numpy as np

driver = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","test"))

config = {
'node_label': 'Pesquisador',
'relationship_type': 'COLABOROU_COM',
'identifier_property': 'id'
}
G = nx.Graph(driver,config)
# %% Pagerank
nx.pagerank(G)
# %% Betweenness centrality
nx.betweenness_centrality(G)


# %% Closeness centrality
nx.closeness_centrality(G)

# %% Componentes conextados

list(nx.connected_components(G))
# %%
