num = int(input())
call = list(map(int, input().split()))


totalStudent = []
for i in range(24):
    totalStudent.append(0)
    
for i in range(num):
    totalStudent[call[i]] += 1

for i in range(1,24):
    print(totalStudent[i],end =" ")