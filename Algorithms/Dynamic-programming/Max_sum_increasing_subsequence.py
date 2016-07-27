This is the extension of longest increasing subsequence

arr = map(int,raw_input().split())
n = len(arr)
t = [0]*n
for i in xrange(n):
	t[i] = arr[i]
for i in xrange(n):
	for j in xrange(i):
		if arr[i]>arr[j] and t[i]<t[j]+arr[i]:
			t[i] = t[j] + arr[i]
print max(t)
