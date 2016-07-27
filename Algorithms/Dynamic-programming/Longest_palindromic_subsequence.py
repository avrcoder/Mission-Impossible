s = raw_input()
n = len(s)
t = [[0]*n for i in xrange(n)]
for i in xrange(n):
	t[i][i] = 1
for i in xrange(2,n+1):
	for j in xrange(n-i+1):
		k = i+j-1
		if s[j] == s[k] and i==2:
			t[j][k] = 2
		elif s[j] == s[k]:
			t[j][k] = t[j+1][k-1] + 2
		else:
			t[j][k] = max(t[j+1][k],t[j][k-1])
print t[0][n-1]
