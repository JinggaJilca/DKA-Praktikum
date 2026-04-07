# Import library yang digunakan 
import matplotlib.pyplot as plt 
import networkx as nx 
# Posisi node yang digunakan pada modul ini 
pos = {'A': [ 0.93888004, -0.0449161 ], 
'B': [-0.73226196, -0.53345128], 
'C': [0.29334637, 1.        ], 
'D': [-0.79991428,  0.56134392], 
'E': [ 0.29994983, -0.98297654]} 

# Fungsi pendukung untuk mencetak graf 
def show_graph(G, pos=None, title='') : 
  if pos == None : 
    pos = nx.spring_layout(G) 
 
  nx.draw( 
      G, 
      pos, 
      with_labels=True, 
      node_color='red', 
      node_size=2000, 
      font_color="white", 
      font_weight="bold", 
      width=5 
  ) 
 
  edge_labels = nx.get_edge_attributes(G, 'weight') 
  nx.draw_networkx_edge_labels( 
      G, 
      pos, 
      edge_labels=edge_labels, 
      font_color='blue', 
      font_weight="bold", 
      font_size=12, 
  ) 
 
  plt.margins(0.2) 
  plt.title(title) 
  plt.show() 


G_undirected = nx.Graph() 
 
# Cetak graf 
show_graph(G_undirected, 
title="Undirected Graph Kosong")

G_directed = nx.DiGraph() 
 
# Cetak graf 
show_graph(G_directed, 
title="Directed Graph Kosong") 