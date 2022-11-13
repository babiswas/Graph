class Node:
   def __init__(self,value):
      self.value=value
      self.rank=0

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=list()

   def add_edges(self,u,v,w):
       self.graph.append((u,v,w))

   def find(self,u,parent):
       if u!=parent[u].value:
          parent[u].value=self.find(parent[u].value,parent)
       return parent[u].value

   def krushkal(self):
       spanning_tree=list()
       parent=[Node(i) for i in range(self.vertex)]
       def get_key(obj):
           return obj[2]
       self.graph=sorted(self.graph,key=get_key)
       for u,v,w in self.graph:
           index1=self.find(u,parent)
           index2=self.find(v,parent)
           if index1!=index2:
              self.union(index1,index2,parent)
              spanning_tree.append((u,v,w))
           else:
              continue
       print(spanning_tree)
           
   def union(self,u,v,parent):
       index1=self.find(u,parent)
       index2=self.find(v,parent)
       if index1!=index2:
          if parent[index1].rank>parent[index2].rank:
             parent[index2].value=index1
             parent[index1].rank+=1
          else:
             parent[index1].value=index2
             parent[index2].rank+=1

if __name__=="__main__":
   graph=Graph(9)
   graph.add_edges(0,1,4)
   graph.add_edges(0,7,8)
   graph.add_edges(1,7,11)
   graph.add_edges(7,6,1)
   graph.add_edges(7,8,7)
   graph.add_edges(6,8,6)
   graph.add_edges(1,2,8)
   graph.add_edges(8,2,2)
   graph.add_edges(6,5,2)
   graph.add_edges(2,5,4)
   graph.add_edges(2,3,7)
   graph.add_edges(5,3,14)
   graph.add_edges(5,4,10)
   graph.add_edges(3,4,9)
   print("Minimum spanning tree is:")
   graph.krushkal()

