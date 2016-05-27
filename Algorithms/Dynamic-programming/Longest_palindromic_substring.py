# your code goes here
# this algorithm uses Dynamic programming approch in which we check for each of the lengths. We create a temporary array p and then periodically update it's values
# Here i is the starting of each of the substrings and j is the ending of each of the substrings and as we move on we are comparing the first and the last chars of the substring
# This algorithms take O(n^2) time.




def palsubstring(s):
	n = len(s)
	p = [[0 for x in range(n)] for y in range(n)]
	for i in range(n):
		p[i][i] = True
	max_len = 1
	leng = 1
	for l in range(2,n+1):
		for i in range(n-l+1):
			j = i+l-1
			if(l==2 and s[i]==s[j]):
				p[i][j] = True
				max_len = 2
			else:
				if(s[i]==s[j] and p[i+1][j-1]):
					p[i][j] = True
					leng = l
				if(leng > max_len): max_len = leng
	return max_len

s = raw_input()
print palsubstring(s)
	
