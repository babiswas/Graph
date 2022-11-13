from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def display(self):
       for j in self.graph:
          print(f"{j}------>{self.graph[j]}")

   def K_core(self,K):
      queue=list()
      while True:
         for i in self.graph:
            if len(self.graph[i])<K:
               queue.append(i)
         if queue:
            for i in queue:
               del self.graph[i]
            for j in self.graph:
               for h in self.graph[j]:
                   if h in queue:
                      self.graph[j].remove(h)
         else:
           break
         queue.clear()

if __name__=="__main__":
   k = 3
   g1 = Graph (9)
   g1.add_edges(0,1)
   g1.add_edges(0,2)
   g1.add_edges(1,2)
   g1.add_edges(1,5)
   g1.add_edges(2,3)
   g1.add_edges(2,4)
   g1.add_edges(2,5)
   g1.add_edges(2,6)
   g1.add_edges(3,4)
   g1.add_edges(3,6)
   g1.add_edges(3,7)
   g1.add_edges(4,6)
   g1.add_edges(4,7)
   g1.add_edges(5,6)
   g1.add_edges(5,8)
   g1.add_edges(6,7)
   g1.add_edges(6,8)
   g1.K_core(3)
   g1.display()
   