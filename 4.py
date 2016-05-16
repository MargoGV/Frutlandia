import networkx as nx
import matplotlib.pyplot as plt
import random as rand




    

def DFS(start):
    flag_list.add(start)
    node_list_for_drawing.append(start)
    for x in nodes_relation[start]:
        if x not in flag_list:
            node_list.remove(x)
            edge_list.append((start,x))
            DFS(x)
            


    
hey=input('Пожалуйста введите имя фала с входными данными: data1, data2, data3, data4\n')   
data=open(hey+'.txt','r')
    


g=nx.Graph()                                          
data_vallue=data.readlines()
edge_list_for_drawing=[]
nodes_relation={}
flag_list=set()

for x in data_vallue:                                
    z=x.split()                                      
    g.add_edge(z[0],z[1],weight=int(z[2]))
    
    if z[0] not in nodes_relation:                    
        nodes_relation[z[0]]=[z[1]]
    else:                                           
        nodes_relation[z[0]].append(z[1])


    if z[1] not in nodes_relation:                 
        nodes_relation[z[1]]=[z[0]]
    else:                                        
        nodes_relation[z[1]].append(z[0])


node_list=g.nodes()
    

pos=nx.spring_layout(g,k=0.8)
k=0
while len(node_list)>0:

    k+=1
    edge_list=[]
    node_list_for_drawing=[]
    DFS(node_list.pop())
    color=rand.choice(['grey','blue','green','red','orange','pink'])
    nx.draw_networkx_nodes(g,pos,
                           nodelist=node_list_for_drawing,
                           node_color=color,
                           node_size=500,
                           alpha=0.7)
    nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list,
                       width=2,
                       edge_color=color,
                       style='solid',
                       alpha=0.7)
                       
                       
nx.draw_networkx_labels(g,pos,
                        font_size=10,
                        font_color='black',
                        font_family='Carlito')


if k==1:
    print('Граф связный')
else:
    print('Граф не связный')
    
plt.axis('off')
plt.savefig("g.png")
plt.show() 




