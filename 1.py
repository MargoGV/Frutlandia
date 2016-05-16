import networkx as nx                                             
import matplotlib.pyplot as plt                                   




data=open('data.txt','r')                                        

g=nx.Graph()                                                      
data_vallue=data.readlines()                                      
node_list=[]                                                      
node_list_painted=[]                                              
edge_list=[]                                                      
edge_list_painted=[]                                              
label_list=set()                                                  
label_list_painted=set()                                                                                           
for i in range(len(data_vallue)):                                 
data=data_vallue[i].split()                                   
    g.add_edge(data[0],data[1],weight=int(data[2]))               
    if data[0]=='Сливовый' or data[1]=='Сливовый' and data[0] not in label_list_painted:            
        node_list_painted.append(data[0])                          
        label_list_painted.add(data[0])                           
        elif data[0] not in label_list:                               
            node_list.append(data[0])                                 
        label_list.add(data[0])                                   
    if data[0]=='Сливовый' or data[1]=='Сливовый'  and data[1] not in label_list_painted:            
        node_list_painted.append(data[1])                          
        label_list_painted.add(data[1])                           
    elif data[1] not in label_list:                               
        node_list.append(data[1])                                
        label_list.add(data[1])                                   
    if data[0]=='Сливовый' or data[1]=='Сливовый'::                  
        edge_list_painted.append((data[0],data[1]))                
    else:
        edge_list.append((data[0],data[1]))                       
      


    
    
    
pos=nx.spring_layout(g,k=0.8)                                     



 
nx.draw_networkx_nodes(g,pos,                                     
                       nodelist=node_list,                       
                       node_color='blue',                         
                       node_size=500,                            
                       alpha=0.2)                                
                       
                 
nx.draw_networkx_edges(g,pos,                                    
                       edgelist=edge_list,                       
                       alpha=0.2,                                
                       width=2,                                 
                       edge_color='blue',                        
                       style='solid')                             
                       
            
nx.draw_networkx_nodes(g,pos,                                     
                       nodelist=node_list_painted,               
                       node_color='yellow',                      
                       node_size=500)                            

           
nx.draw_networkx_edges(g,pos,                                     
                       edgelist=edge_list_painted,                
                       width=2,                                  
                       edge_color='yellow',                       
                       style='solid')                             

                     
nx.draw_networkx_nodes(g,pos,                                     
                       nodelist=['Фейхоа'],                      
                       node_color='red',                         
                       node_size=500)                             


nx.draw_networkx_labels(g,pos=pos,                               
                        font_size=10,                             
                        font_color='black',                       
                        font_family='Carlito')                   


plt.axis('off')                                                   
plt.savefig("g.png")                                              
plt.show()                                                       
