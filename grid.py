class Cycle:
  def __init__(self,x,y,count):
      self.x=x
      self.y=y
      self.count=count

def is_valid(x,y,N):
   if x<0 or x>=N:
      return False
   if y<0 or y>=N:
      return False
   return True

def find_steps(N,x,y,target_x,target_y):
    queue=list()
    visited=[[False for i in range(N)] for i in range(N)]
    queue.append(Cycle(x,y,0))
    visited[x][y]=True
    dx=[2,2,-2,-2,1,-1,1,-1]
    dy=[1,-1,1,-1,2,2,-2,-2]
    while queue:
        m=queue.pop(0)
        if m.x==target_x and m.y==target_y:
           return m.count
        for i in range(8):
            X=dx[i]+m.x
            Y=dy[i]+m.y
            if is_valid(X,Y,N) and visited[X][Y]==False:
               queue.append(Cycle(X,Y,m.count+1))
               visited[X][Y]=True

if __name__=="__main__":
  print(find_steps(30,1,1,28,28))
  

  
        
   