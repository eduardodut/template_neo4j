# template_neo4j
 
guia:

https://medium.com/neo4j/nxneo4j-networkx-api-for-neo4j-a-new-chapter-9fc65ddab222

Software necessário:

Docker - https://docs.docker.com/docker-for-windows/install/

Neo4j desktop - https://neo4j.com/download/

Vscode - https://code.visualstudio.com/download
    extensões: docker, jupyter, html preview

Miniconda ou Anaconda - https://docs.conda.io/en/latest/miniconda.html

Instalação do ambiente:

```
# no terminal
conda env create --name template_neo4j python=3.7
conda activate template_neo4j
pip install neo4j, wget, pandas, git+https://github.com/ybaktir/networkx-neo4j
```

Download dos datasets:

download_dados.py

Exemplo de carregamento de dados:

insert.py


Exemplo de leitura e aplicação de algoritmos:

read.py
