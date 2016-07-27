It's  a slight modification of LIS problem as it includes LIS as well as LDS(longest decresing subsequnce)

arr = map(int,raw_input().split())
n = len(arr)
lis = [1]*n
for i in xrange(1,n):
	for j in xrange(i):
		if arr[i]>arr[j] and lis[i]<lis[j]+1:
			lis[i] = lis[j] + 1
lds = [1]*n
for i in xrange(n-2,-1,-1):
	for j in xrange(n-1,i,-1):
		if arr[i]>arr[j] and lds[i]<lds[j]+1:
			lds[i] = lds[j] + 1
m = lds[0] + lis[0] - 1
for i in xrange(1,n):
	m = max(m,lis[i] + lds[i] - 1)
print m
