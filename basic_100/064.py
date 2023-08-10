num_1, num_2, num_3 = map(int, input().split())

result = num_1 if(num_1<=num_2 and num_1 <= num_3) else num_2 if(num_2<=num_3 and num_2 <= num_1) else num_3 if(num_3<=num_1 and num_3 <= num_2) else 0

print(result)