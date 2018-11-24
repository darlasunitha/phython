num = raw_input().rstrip()
sLen = len(num)
mid = sLen >> 1
if (sLen & 1):
	print(num[:mid] + "*" + num[mid+1:])
else:
	print(num[:mid-1] + "**" + num[mid+1:])
