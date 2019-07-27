import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
jishu=0
G=nx.Graph()
data = pd.read_csv('./FPKM_cufflinks.tsv', sep='\t')
index = data["Ensembl_gene_id"]
data= data.drop("Ensembl_gene_id",axis=1)
data = data.dropna(axis=0)
edge_color = list()
for i in range(data.shape[0]):
    for j in range(i+1,data.shape[0]):
        x = data[i:i+1]
        y = data[j:j+1]
        t = np.corrcoef(x,y)
        print(jishu)
        if t[0][1] >0.85 :
            G.add_edge(i,j)
            edge_color.append("red")
            pos = nx.circular_layout(G)
            nx.draw(G,pos,with_labels=True,node_size = 50,node_color = "blue",edge_color = edge_color)
            jishu+=1
            if jishu%100==0 : plt.show()
        elif t[0][1] < -0.85 :
            G.add_edge(i,j)
            edge_color.append("blue")
            pos = nx.circular_layout(G)
            nx.draw(G,pos,with_labels=True,node_size = 50,node_color = "blue",edge_color = edge_color)
            jishu+=1
            if jishu%100==0 : plt.show()
plt.show()