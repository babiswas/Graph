#DFS 
from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)

   def dfs_util(self,visited,u):
       visited[u]=True
       print(u)
       for i in self.graph[u]:
          if not visited[i]:
             self.dfs_util(visited,i)

   def dfs(self,u):
       visited=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
             self.dfs_util(visited,i)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print("The dfs traversal of the graph is:")
   graph.dfs(2)
             