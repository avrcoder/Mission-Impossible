val = map(int,raw_input().split())
l = input()
t = [0]*(l+1)
for i in xrange(1,l+1):
	for j in xrange(i,l+1):
		t[j] = max(t[j],val[i-1]+t[j-i])
print t[l]
