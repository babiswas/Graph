from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)


   def find_shortest(self,u,v):
       prev=self.find(u,v)
       path=list()
       index=v
       while index!=None:
           path.append(index)
           index=prev[index]
       path=path[::-1]
       print(path)
       if path[0]==u:
          print(f"There is a path from {u} to {v}")
          print(path)
       else:
          print(f"There is no path from {u} to {v}")

   def find(self,u,v):
       prev=[None]*self.vertex
       queue=list()
       visited=[False]*self.vertex
       queue.append(u)
       visited[u]=True
       while queue:
           m=queue.pop(0)
           for i in self.graph[m]:
              if not visited[i]:
                 visited[i]=True
                 queue.append(i)
                 prev[i]=m
       print(prev)
       return prev

if __name__=="__main__":
   graph=Graph(8)
   graph.add_edges(1,2)
   graph.add_edges(1,0)
   graph.add_edges(0,3)
   graph.add_edges(3,7)
   graph.add_edges(3,4)
   graph.add_edges(7,4)
   graph.add_edges(7,6)
   graph.add_edges(4,5)
   graph.add_edges(6,5)
   graph.add_edges(4,6)
   print("The shortest path is:")
   graph.find_shortest(0,7)


           