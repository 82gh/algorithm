num_1, num_2, num_3 = map(int, input().split())

for i in range(0,num_1):
  for j in range(0,num_2):
    for k in range(0,num_3):
      print(i,j,k,sep=" ")
print(num_1 * num_2 * num_3)