import sys
def dkstra(M,vertex,src):
    parent=[-1]*vertex
    cost=[sys.maxsize]*vertex
    visited=[False]*vertex
    cost[src]=0
    def find_min_cost(visited,cost):
        min=sys.maxsize
        index=0
        for i in range(vertex):
            if cost[i]<min and visited[i]==False:
               min=cost[i]
               index=i
        return index
    for i in range(vertex):
       index=find_min_cost(visited,cost)
       for i in range(vertex):
         if cost[index]+M[index][i]<cost[i] and M[index][i]!=0 and visited[i]==False:
            cost[i]=M[index][i]+cost[index]
            parent[i]=index
       visited[index]=True
    print(parent)
    print(cost)

if __name__=="__main__":
   print("The shortest path algorithm is:")
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
  
   

       
      