import re
from collections import deque, defaultdict
from string import ascii_uppercase

INPUT_EXP = r'Step ([A-Z]+) must be finished before step ([A-Z]+) can begin\.'

def read_file(filename):
	dependencies = defaultdict(list)
	neighbours = defaultdict(list)
	nodes = set()
	with open(filename) as f:
		for line in f.readlines():
			v1, v2 = re.findall(INPUT_EXP, line.strip())[0]
			dependencies[v2].append(v1)
			neighbours[v1].append(v2)
			
			nodes.add(v1)
			nodes.add(v2)
	return dependencies, neighbours, nodes

def topological_sort(dependencies, neighbours, nodes):
	output = []
	start_queue = deque(sorted((node for node in nodes if node not in dependencies)))
	
	while start_queue:
		
		node = start_queue.popleft()
		output.append(node)
		for neighbour in neighbours[node]:
			if all(n in output for n in dependencies[neighbour]) and neighbour not in start_queue:
				start_queue.append(neighbour)

		start_queue = deque(sorted(start_queue))

	return ''.join(output)

step_seconds = {ch:i+1 for i, ch in enumerate(ascii_uppercase)}

connections, neighbours, nodes = read_file('day7-sample-input.txt')

sortedorder = topological_sort(connections, neighbours, nodes)
print(sortedorder)
totseconds = 0
for task in sortedorder:
	totseconds += step_seconds[task]

print(totseconds)








