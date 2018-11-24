num=int(raw_input())
factor=0
for i in range(1,num):
    if num%i==0:
        factor=i
if factor>1:
    print "yes"
else:
    print "no"
