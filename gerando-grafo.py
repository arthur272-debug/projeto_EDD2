import pandas as pd;
import networkx as nx;
from networkx.algorithms import community;
from geopy.distance import distance;
import numpy as np;
import matplotlib.pyplot as plt

caminho_bases = "/content/drive/MyDrive/projeto_edd2/bases_de_dados/";

base = pd.read_csv(f"{caminho_bases}base.csv");

# gera um array de arrays com todos os registros da base
escolas = base.to_numpy();

# posiçao dos atributos em cada array;
latitude = len(escolas[0]) - 2;
longitude = len(escolas[0]) - 1;
id_escola = 1;
nota_ideb = 2;
nome_escola = 3;
sigla_uf = 5;
regiao = 6;
municipio = 7;
bairro = 8; 

grafo = nx.Graph();

i = 0;

for escola in escolas:

  grafo.add_node(
    i, 
    escola=escola[id_escola], 
    nome=escola[nome_escola], 
    ideb=escola[nota_ideb], 
    sigla_uf=escola[sigla_uf], 
    regiao=escola[regiao], 
    municipio=escola[municipio], 
    bairro=escola[bairro], 
    latitude=escola[latitude], 
    longitude=escola[longitude]
  );

  i += 1;
  
escolas = grafo.nodes;
total_escolas = len(escolas);

for i in range(total_escolas):
  
  latitude1 = escolas[i]["latitude"];
  longitude1 = escolas[i]["longitude"];

  coordenada1 = (latitude1, longitude1);

  ultimo_municipio_analisado = ""

  for j in range(i, total_escolas):

    if (i == j):
      continue;

    latitude2 = escolas[j]["latitude"];
    longitude2 = escolas[j]["longitude"];


    coordenada2 = (latitude2, longitude2);

    distancia = distance(coordenada1, coordenada2).km;
    
    if distancia <= 10:
      grafo.add_edge(i, j, distancia=distancia);
      
nx.draw(grafo, pos=nx.random_layout(grafo), with_labels=False, node_size=10);
plt.show();

print(nx.numeric_assortativity_coefficient(grafo, "ideb"));

communities_generator = community.girvan_newman(grafo);
communities = next(communities_generator);

comunidades = sorted(map(sorted, communities))
print(comunidades);