v = 4
INF = 999
def floydWarshall(graph):
	dist = [[0]*v for i in xrange(v)]
	for i in xrange(v):
		for j in xrange(v):
			dist[i][j] = graph[i][j]
	for k in xrange(v):
		for i in xrange(v):
			for j in xrange(v):
				if dist[i][j]>dist[i][k] + dist[k][j]:
					dist[i][j] = dist[i][k] + dist[k][j]
	for i in xrange(v):
		for j in xrange(v):
			if dist[i][j] == INF:
				print INF,
			else:
				print dist[i][j],
		print

graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
floydWarshall(graph)
