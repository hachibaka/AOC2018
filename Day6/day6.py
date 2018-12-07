def read_file(filename):
	with open(filename) as f:
		points = [tuple(map(int,x.strip().split(','))) for x in f.readlines()]
	return points


def find_max_x_y(points):
	x = max(x[0] for x in points)
	y = max(x[1] for x in points)
	return max(x, y)

def manhattan_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def points_distribution(points, square_size):
	manhattan_points = {}

	
	for i in range(square_size+1):
		for j in range(square_size+1):
			
			_dist_points = {}
			for k, point in enumerate(points):
				dist = manhattan_distance((j,i), point)
				if dist in _dist_points:
					_dist_points[dist].append(k)
				else:
					_dist_points[dist] = [k]
			
			min_dist = min(_dist_points.keys())
			#print("Minimum distance for point {}, {} is {} for label {}".format(j,i, min_dist,_dist_points[min_dist]))
			if len(_dist_points[min_dist]) > 1:
				manhattan_points[(j, i)] =  '.'
			else:
				manhattan_points[(j, i)] = _dist_points[min_dist][0]
						

	return manhattan_points

def print_mahattan_points(m_points, square_size):
	print('     ',end='')
	for i in range(square_size+1):
		print(i,sep=' ',end='')
	print()
	for i in range(square_size+1):
		print(i,'-->',end='')
		for j in range(square_size+1):

			print(manhattan_points[(j,i)], sep=' ',end='')
		print()


def find_longest_distance(m_points, square_size, num_of_points):

	_points_area = {}
	for point, label in m_points.items():
		if (point[0] == 0 or point[0] == square_size or point[1] == 0 or point[1] == square_size ):
			_points_area[label] = -1
		elif label in _points_area and _points_area[label] == -1:
			continue
		else:
			_points_area[label] = _points_area.get(label,0) + 1


	max_distance = -1
	max_label = None
	for label, area  in _points_area.items():
		if max_distance < area:
			max_distance = area
			max_label = label


	return max_distance, max_label

			

points = read_file('day6-input.txt')
num_of_points = len(points)
#print(points)
square_size = find_max_x_y(points)

manhattan_points = points_distribution(points, square_size)
#print(manhattan_points)

print("Max Distance not infinite is ", find_longest_distance(manhattan_points, square_size, num_of_points))

#print_mahattan_points(manhattan_points, square_size)









