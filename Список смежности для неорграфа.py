
edges = [[1, 2], [1, 4], [1, 8], [1, 10], [2, 3], [2, 6], [3, 5], [3, 10], [5, 6], [5, 7], [6, 9], [7, 9]]
for i in range(1, 11):
	e = []
	for z in edges[:]:
		e.append(z[:])
	out = []
	for j in e:
		if i in j:
			j.remove(i)
			out.append(j[0])
	s = ', '.join(str(n) for n in out)
	print(f'{i}: {s}')
