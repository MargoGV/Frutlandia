# Задание 3 отобразить остовное дерево методом обходы в глубину(DFS)
import networkx as nx
import matplotlib.pyplot as plt




def DFS(start):
    flag_list.add(start)
    for x in nodes_relation[start]:
        if x not in flag_list:
            edge_list_for_drawing.append((start,x))
            DFS(x)
    



data=open('data1.txt','r')


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
        
        
print('\n'.join(g.nodes()))
       
hey=input('Пожалуйста, введите превую вершину(из предложенных выше)\n')
    
DFS(hey) 
    



pos=nx.spring_layout(g,k=0.8)


nx.draw_networkx_nodes(g,pos,
                       node_color='green',
                       node_size=500,
                       alpha=0.7)
                   
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list_for_drawing,
                       width=2,
                       edge_color='green',
                       style='solid',
                       alpha=0.7)
nx.draw_networkx_labels(g,pos,
                        font_size=10,
                        font_color='black',
                        font_family='Carlito')


    
    
plt.axis('off')
plt.savefig("g.png")
plt.show() 
    
