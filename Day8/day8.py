def read_file(filename):
	with open(filename) as f:
		licence = list(map(int, f.read().strip().split()))
	return licence


def parse_licence(licence):
	stack = []
	node_data = {}
	nodes = 0
	node_started = False
	licence_length = len(licence)
	check_sum = 0
	i = 0
	while i < licence_length:
		#print(i, nodes, stack, node_data)
		num_children = licence[i]
		num_metadata_entry = licence[i+1]
		i += 2
		if num_children == 0:

			if stack:
				stack[-1][3].append(nodes)
			node_data[nodes] = {'num_of_children': num_children, 'metadata' : licence[i:i+num_metadata_entry], 'children':[]}
			nodes += 1
			check_sum += sum(licence[i:i+num_metadata_entry])
			i += num_metadata_entry
			if stack:
				stack[-1][0] -= 1

			while stack and stack[-1][0] == 0:
				nofchildren , nofmetadata, nodeid, children = stack.pop()
				node_data[nodeid] = {'num_of_children': nofchildren, 'metadata' : licence[i:i+nofmetadata],'children': children}
				check_sum += sum(licence[i:i+nofmetadata])
				i += nofmetadata
				if stack:
					stack[-1][0] -= 1

		else:
			if stack:
				stack[-1][3].append(nodes)
			stack.append([num_children,num_metadata_entry, nodes, []])
			nodes += 1

	return check_sum, node_data


def find_root_value(node,  node_data):
	
	if node not in node_data:
		return 0
	if not node_data[node]['children']:
		return sum(node_data[node]['metadata'])
	nodesum = 0
	for childnode in node_data[node]['metadata']:
		if childnode <= len(node_data[node]['children']):
			nodesum += find_root_value(node_data[node]['children'][childnode-1], node_data)

	return nodesum 

		

		

licence = read_file('day8-input.txt')		
check_sum, tree = parse_licence(licence)
print("Part1 - Check sum of parsed tree ", check_sum)
#print("Tree is ", tree)
print("Part2 - Root value", find_root_value(0, tree))