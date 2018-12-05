def read_file(filename):
	with open(filename) as f:
		polymer = ''.join(x.strip() for x in f.readlines())

	return polymer

def isidentical(ch1, ch2):
	return abs(ord(ch1) - ord(ch2)) == 32

def alchmist_reduction_part1(polymer):
	stack = []
	for ch in polymer:
		if not stack:
			stack.append(ch)
		elif isidentical(stack[-1], ch):
			stack.pop()
		else:
			stack.append(ch)

	return len(stack)


def alchmist_reduction_part2(polymer):
	
	minlength = 99999999
	
	unique_units = set(polymer.lower())
	for unit in unique_units:
		stack = []
		for ch in polymer:
			if not (ch == unit or isidentical(ch, unit)):
				if not stack:
					stack.append(ch)
				elif isidentical(stack[-1], ch):
					stack.pop()
				else:
					stack.append(ch)
		stacklength = len(stack)
		if minlength > stacklength:
			minlength = stacklength
			

	return minlength



polymer = read_file('day5-input.txt')

print("Length of Polymer after reduction is ", alchmist_reduction_part1(polymer))
print("Shortest Length of Polymer after reduction is ", alchmist_reduction_part2(polymer))