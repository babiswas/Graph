from collections import defaultdict

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def cyclic_util(self,visited,u,parent):
       visited[u]=True
       for i in self.graph[u]:
         if visited[i]==False:
            if self.cyclic_util(visited,i,u):
               return True
         elif i!=parent:
             return True
       return False  

   def iscyclic(self):
       visited=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
            if self.cyclic_util(visited,i,-1):
               return True
       return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   print("Find cycle in the graph:")
   print(graph.iscyclic())
