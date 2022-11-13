class Node:
   def __init__(self,value):
      self.value=value
      self.rank=0

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=list()

   def add_edges(self,u,v):
      self.graph.append((u,v))

   def find(self,u,parent):
       while parent[u].value!=u:
            u=parent[u].value
       return u

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

   def detect_cycle(self):
       parent=[Node(i) for i in range(self.vertex)]
       for u,v in self.graph:
          index1=self.find(u,parent)
          index2=self.find(v,parent)
          if index1!=index2:
             self.union(index1,index2,parent)
          else:
             return True
       return False
       
if __name__=="__main__":
  print("Detect cycle in graph:")
  graph=Graph(6)
  graph.add_edges(5,0)
  graph.add_edges(4,0)
  graph.add_edges(5,2)
  graph.add_edges(2,3)
  graph.add_edges(3,1)	
  print(graph.detect_cycle())



