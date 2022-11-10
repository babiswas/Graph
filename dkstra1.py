import heapq
import sys

def dkstra(M,vertex,src):
    parent=[-1]*vertex
    cost=[sys.maxsize-1]*vertex
    visited=[False]*vertex
    l=list()
    heapq.heapify(l)
    heapq.heappush(l,(M[src][src],-1,src))
    cost[src]=M[src][src]
    while len(l)!=0:
        item=heapq.heappop(l)
        source=item[2]
        if visited[source]==False:
           parent[source]=item[1]
           cos=item[0]
           visited[source]=True
           for i in range(vertex):
              if (visited[i]==False) and (M[source][i]+cos<cost[i]) and (M[source][i]!=0):
                 cost[i]=M[source][i]+cos
                 heapq.heappush(l,(cost[i],source,i))
    print(parent)
    print(cost)

if __name__=="__main__":
   print("The shortest path algorithm:")
   a=[0, 4, 0, 0, 0, 0, 0, 8, 0]
   b=[4, 0, 8, 0, 0, 0, 0, 11, 0]
   c=[0, 8, 0, 7, 0, 4, 0, 0, 2]
   d=[0, 0, 7, 0, 9, 14, 0, 0, 0]
   e=[0, 0, 0, 9, 0, 10, 0, 0, 0]
   f=[0, 0, 4, 14, 10, 0, 2, 0, 0]
   g=[0, 0, 0, 0, 0, 2, 0, 1, 6]
   h=[8, 11, 0, 0, 0, 0, 1, 0, 7]
   i=[0, 0, 2, 0, 0, 0, 6, 7, 0]
   M=[a,b,c,d,e,f,g,h,i]
   dkstra(M,9,0)
  
   
   
   
                 
        
    
    
    