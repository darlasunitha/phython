n=int(raw_input())
sum=0
num=n
 
while n!=0:
	rem=n%10
	sum=sum*10+rem
	n=n/10
if sum==num:
	print "yes"
else:
	print "no"
 
