
# To enter multiple inputs in a single line we use this map map(int,raw_input().split())

l = map(int,raw_input().split());

# To create a matrix in python. For a two dimensional matrix we have [[0 for x in range(w)]for y in range(v)]

fib = [0 for x in range(l[2])]
fib[0] = l[0]
fib[1] = l[1]
for i in range(2,l[2]):
	fib[i] = fib[i-1]*fib[i-1] + fib[i-2]
print fib[l[2]-1]
