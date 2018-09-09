n = int(raw_input())
 
length = len(str(n))
sum = 0
temp = n
 
while(temp != 0):
    sum = sum + ((temp % 10) ** length)
    temp = temp // 10
 
if sum == n:
    print("yes")
else:
    print("no")
