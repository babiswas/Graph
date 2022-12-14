class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=list()

   def add_edges(self,u,v):
      self.graph.append((u,v))

   def find(self,u,parent):
       while parent[u]!=-1:
          u=parent[u]
       return u

   def union(self,u,v,parent):
      index1=self.find(u,parent)
      index2=self.find(v,parent)
      if index1!=index2:
         parent[u]=v

   def detect_cycle(self):
       parent=[-1]*self.vertex
       for u,v in self.graph:
          print(parent)
          index1=self.find(u,parent)
          index2=self.find(v,parent)
          if index1!=index2:
             self.union(index1,index2,parent)
          else:
             return True
       return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(4,1)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   print(graph.detect_cycle())
   print("Creating a new graph")
   graph1=Graph(6)
   graph1.add_edges(5,0)
   graph1.add_edges(4,0)
   graph1.add_edges(4,1)
   graph1.add_edges(5,2)
   graph1.add_edges(2,3)
   graph1.add_edges(3,1)
   print(graph1.detect_cycle())
  
   

