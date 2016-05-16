import networkx as nx
import matplotlib.pyplot as plt




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


count_of_way_to={}

for x in g.nodes():
    count_of_way_to[x]=None
    
hey=input('Введите название желаемой вершины(одной из представленных выше)\n')
hey1=hey

count_of_way_to[hey]=0
while len(unflag_list)>0:
    unflag_list.remove(hey)
    for x in nodes_relation[hey]:
        if (x in unflag_list) and (count_of_way_to[x]==None or count_of_way_to[x]>count_of_way_to[hey]+weight_dict[hey][x]):
            count_of_way_to[x]=count_of_way_to[hey]+weight_dict[hey][x]
    min=None
    for x in unflag_list:
        if (count_of_way_to[x]!=None) and(min==None or count_of_way_to[x]<min):
            min=count_of_way_to[x]
            hey=x
    if k>len(g.nodes(+10)):
        print('граф не связный')
        break


for x in count_of_way_to:
    print('Длина кратчайшего пути от вершины',hey1,'до вершины',x,'равна:',count_of_way_to[x])
    
        


                       
                       



            
    
    
