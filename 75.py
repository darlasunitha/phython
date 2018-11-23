x = raw_input().rstrip()
sLen = len(x)
mid = sLen >> 1
if (sLen & 1):
	print(x[:mid] + "*" + x[mid+1:])
else:
	print(x[:mid-1] + "**" + x[mid+1:])
