from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def mother_util(self,visited,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.mother_util(visited,i)

   def mother(self):
       index=0
       visited=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
             self.mother_util(visited,i)
             index=i
       print(visited)
       visited=[False]*self.vertex
       self.mother_util(visited,index)
       if False in visited:
          print("There is no mother vertex in the graph:")
       else:
          print(f"{index} is the mother vertex")

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print("The mother vertex of the graph is:")
   graph.mother()
             