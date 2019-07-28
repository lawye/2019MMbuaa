import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from IPython.core.pylabtools import figsize

plt.rcParams['figure.figsize'] = (15,15)#调节大小
plt.rcParams['savefig.dpi'] = 80#调节大小
plt.rcParams['figure.dpi'] = 80#调节大小

G=nx.Graph() #创建空图
data = pd.read_csv('./FPKM_cufflinks.tsv', sep='\t') #读入数据
#数据处理
index = data["Ensembl_gene_id"]
data= data.drop("Ensembl_gene_id",axis=1)
data = data.dropna(axis=0)
edge_color = list()
count = 0
co=0
f = open('data2.tsv','w')
for i in range(data.shape[0]):
    for j in range(i+1,data.shape[0]):
        co+=1
        print(str(co)+' '+str(count))
        #以下读取两行 计算相关系数t
        x = data[i:i+1]
        y = data[j:j+1]
        t = np.corrcoef(x,y)
        if t[0][1] > 0.9 or t[0][1] < -0.9:
            f.write(str(count) + '\t' + str(i) + '\t' + str(j)+'\t'+index[i] + '\t'+ index[j] + '\t'+str(t[0][1]) + '\n')
            count +=1
f.close()

'''


for i in range(data.shape[0]):
    for j in range(i+1,data.shape[0]):
        #以下读取两行 计算相关系数t
        x = data[i:i+1]
        y = data[j:j+1]
        t = np.corrcoef(x,y)
        if t[0][1] >0.9:
            G.add_edge(i,j) #向图中导入边
            edge_color.append("red")#记录颜色 
            count +=1
        elif t[0][1] < -0.9:
            G.add_edge(i,j)#向图中导入边
            edge_color.append("blue")#记录颜色 
            count +=1
            
        if count%100 ==0:
            pos = nx.circular_layout(G)  #图中的点呈环形分布
            nx.draw(G,pos,with_labels=True,node_size = 1,node_color = "#bb99ff",edge_color = edge_color,width = 0.1,font_size = 1,font_color="black")# 画图,设置相关属性
            plt.savefig('plot'+str(count)+'.png', dpi=300)  #存图
            print(count)
            
'''