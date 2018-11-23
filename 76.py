k=int(raw_input())
factor=0
for x in range(1,k):
    if k%x==0:
        factor=x
if factor>1:
    print "yes"
else:
    print "no"
