# Здание номер два, остроить и отобразить остовное дерево методом обхода в ширину(BFS)

import networkx as nx                                                   
import matplotlib.pyplot as plt                                        


data=open('data.txt','r')                             

g=nx.Graph()                                          
data_vallue=data.readlines()                          
edge_list_for_drawing=[]                              
nodes_relation={}                                     


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


stack=['']*len(g.nodes())                             
flag_dict=set()                                       
first=0                                               
last=1                                                
stack[first]=hey                                      
while first<last:                                     
    node=stack[first]                                 
    flag_dict.add(node)                               
    first+=1                                          
    for x in nodes_relation[node]:                    
        if x not in flag_dict:                        
            edge_list_for_drawing.append((node,x))    
            flag_dict.add(x)                          
            stack[last]=x                             
            last+=1                                   
            
            
    

pos=nx.spring_layout(g,k=0.8)



nx.draw_networkx_nodes(g,pos,
                       node_color='g',
                       node_size=500,
                       alpha=0.7)
                   
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list_for_drawing,
                       width=2,
                       edge_color='g',
                       style='solid',
                       alpha=0.7)
nx.draw_networkx_labels(g,pos,
                        font_size=10,
                        font_color='black',
                        font_family='Carlito')


    
    
plt.axis('off')
plt.savefig("g.png")
plt.show() 
    
    

