import networkx as nx
import matplotlib.pyplot as plt
import random as rand




data=open('data.txt','r')

g=nx.Graph() 
k=0
data_vallue=data.readlines()
nodes_relation={}
weight_dict={}
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
    
    if z[0] not in weight_dict:                 
        weight_dict[z[0]]={z[1]:int(z[2])}
    else:                                        
        weight_dict[z[0]][z[1]]=int(z[2])
    
    if z[1] not in weight_dict:                 
        weight_dict[z[1]]={z[0]:int(z[2])}
    else:                                        
        weight_dict[z[1]][z[0]]=int(z[2])
    
        
    
        
unflag_list=g.nodes()

print('\n'.join(g.nodes()))

way_to={}
count_of_way_to={}

for x in g.nodes():
    way_to[x]=None
    count_of_way_to[x]=None
    
hey=input('Введите название начальной вершины(одной из представленных выше)\n')
end=input('Введите название конечной вершины(одной из представленных выше)\n')
hey1=hey
way_to[hey]=[hey]
count_of_way_to[hey]=0
while len(unflag_list)>0:
    unflag_list.remove(hey)
    for x in nodes_relation[hey]:
        if (x in unflag_list) and (count_of_way_to[x]==None or count_of_way_to[x]>count_of_way_to[hey]+weight_dict[hey][x]):
            count_of_way_to[x]=count_of_way_to[hey]+weight_dict[hey][x]
            way_to[x]=[]
            way_to[x].extend(way_to[hey])
            way_to[x].append(hey)
    min=None
    for x in unflag_list:
        if (count_of_way_to[x]!=None) and(min==None or count_of_way_to[x]<min):
            min=count_of_way_to[x]
            hey=x
    if hey==end:
        break
    


way_to[end].append(end)
print(way_to[end])
edge_list=[]
for i in range(len(way_to[end])-1):
    edge_list.append((way_to[end][i],way_to[end][i+1]))


pos=nx.spring_layout(g,k=0.8)


nx.draw_networkx_nodes(g,pos,
                       node_color='blue',
                       node_size=500,
                       alpha=0.7)
                   
nx.draw_networkx_edges(g,pos,
                       width=2,edge_color='blue',style='solid',
                       alpha=0.7)

nx.draw_networkx_nodes(g,pos,
                       nodelist=way_to[end],
                       node_color='green',
                       node_size=500,
                       alpha=1)
                       
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list,
                       width=5,edge_color='green',style='solid',
                       alpha=1)
nx.draw_networkx_labels(g,pos,font_size=10,font_color='black',font_family='Carlito')




plt.axis('off')
plt.savefig("g.png")
plt.show() 

    






