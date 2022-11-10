from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def kahns_algo(self):
       queue=list()
       count=0
       inner=[0]*self.vertex
       for i in self.graph:
         for j in self.graph[i]:
            inner[j]+=1
       for i in range(self.vertex):
         if inner[i]==0:
            queue.append(i)
       while queue:
          m=queue.pop(0)
          print(m)
          for i in self.graph[m]:
             inner[i]-=1
             if inner[i]==0:
                queue.append(i)
          count+=1
       if count==self.vertex:
          print("Topological sort is possible:")
       else:
          print("There is a cycle in the graph:")

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   print("Kahns topological sort:")
   graph.kahns_algo()
   graph1=Graph(4)
   graph1.add_edges(0,2)
   graph1.add_edges(2,0)
   graph1.add_edges(0,1)
   graph1.add_edges(1,2)
   graph1.add_edges(2,3)
   graph1.add_edges(3,3)
   print("Topological sorting:")
   graph1.kahns_algo()
   
   


          
          
       