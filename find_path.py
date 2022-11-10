from collections import defaultdict

class Graph:
  def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

  def add_edges(self,u,v):
      self.graph[u].append(v)

  def path(self,u,v):
      path=list()
      visited=[False]*self.vertex
      self.path_util(visited,u,v,path)

  def path_util(self,visited,u,v,path):
      visited[u]=True
      path.append(u)
      if u==v:
         print(path)
      else:
         for i in self.graph[u]:
            if not visited[i]:
               self.path_util(visited,i,v,path)
      path.pop()
      visited[u]=False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(1,3)
   graph.add_edges(3,3)
   print("Find the path from 2 to 3:")
   graph.path(2,3)
      