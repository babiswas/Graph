class Cell:
  def __init__(self,x,count):
      self.x=x
      self.count=count

def issafe(x,N):
   if x<0 or x>=N:
      return False
   return True

def min_end(arr,N):
   dx=[-1,1]
   queue=list()
   queue.append(Cell(0,0))
   visited=[False]*N
   visited[0]=True
   while queue:
      m=queue.pop(0)
      if m.x==len(arr)-1:
         return m.count
      for i in range(2):
         X=m.x+dx[i]
         if issafe(X,len(arr)) and visited[X]==False:
            queue.append(Cell(X,m.count+1))
            visited[X]=True
      index=[i for i,j in enumerate(arr) if j==arr[m.x]]
      index.remove(m.x)
      for i in index:
         if visited[i]==False and issafe(i,len(arr)):
            queue.append(Cell(i,m.count+1))
            visited[i]=True
   return -1

if __name__=="__main__":
   arr=[0,1,2,3,4,5,6,7,5,4,3,6,0,1,2,3,4,5,7]
   N=len(arr)
   print(min_end(arr,len(arr)))

         
         
