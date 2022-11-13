def step_num(n,m,nm,s):
   queue=list()
   queue.append(nm)
   while queue:
      num=queue.pop(0)
      if num>=n and num<=m and (num not in s):
         print(num)
         s.add(num)
      if num<n or num>m:		
         continue
      
      temp=num%10

      if temp==0 and ((num*10+temp+1) not in s):
         queue.append(num*10+temp+1)
      elif temp==9 and ((num*10+temp-1) not in s):
         queue.append(num*10+temp-1)
      else:
         if ((num*10+temp-1) not in s):
             queue.append(num*10+temp+1)
         if ((num*10+temp-1) not in s):
             queue.append(num*10+temp-1)

def print_all_stepping_num(n,m,s):
   for i in range(0,10):
       step_num(n,m,i,s)
     

if __name__=="__main__":
  s=set()
  print_all_stepping_num(0,21,s)
   
      