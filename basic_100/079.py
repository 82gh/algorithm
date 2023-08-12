num = int(input())
sum = 0
cnt = 1
while sum < num:
    sum += cnt
    if(sum >= num):
        print(cnt)
        break

    cnt += 1
    

'''
n = int(input())

s = 0
t = 0
while s<n :
  t = t+1
  s = s+t
  
print(t)
'''