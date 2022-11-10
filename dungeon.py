class Cell:
   def __init__(self,x,y,count):
       self.x=x
       self.y=y
       self.count=count

def is_safe(x,y,N,M):
    if x<0 or x>=N:
       return False
    if y<0 or y>=N:
       return False
    if M[x][y]=='#':
       return False
    return True


def min_steps(x,y,M,N,target_x,target_y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=list()
    visited=[[False for i in range(N)] for i in range(N)]
    cell=Cell(x,y,0)
    queue.append(cell)
    visited[x][y]=True
    while queue:
       m=queue.pop(0)
       if m.x==target_x and m.y==target_y:
          return m.count
       for i in range(4):
          X=dx[i]+m.x
          Y=dy[i]+m.y
          if is_safe(X,Y,N,M) and visited[X][Y]==False:
             queue.append(Cell(X,Y,m.count+1))
             visited[X][Y]=True

if __name__=="__main__":
   M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
   print("Minimum steps to reach target:")
   steps=min_steps(0,2,M,4,2,0)
   print(f"{steps} to reach the target:")
   


