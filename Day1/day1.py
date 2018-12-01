import bisect

def part1_tot_freq():
	with open('input-part1.txt') as f:
		totalsum = sum(int(x.strip()) for x in f.readlines() )

	return totalsum


def part2_first_freq(filename):
	seenfreq = [0]
	start = 0
	with open(filename) as f:
		freqlist = [int(x.strip()) for x in f.readlines()]
			
	
	maxindex = len(freqlist)
	print("Length of list is ",maxindex)
	listloopcounter = i = 0
	while True:
		if i == maxindex:
			i = 0
			listloopcounter +=1
			print("Number of time list has been looped is {} and start is {}".format(listloopcounter,start))
		start += freqlist[i]
		i+=1
		position = bisect.bisect(seenfreq, start)
		if seenfreq[position-1] == start:
			return start
		else:
			bisect.insort(seenfreq, start)
			
			



if __name__ == "__main__":
	print("total sum of frequency is ",part1_tot_freq())
	print("First frequency seen twice is ",part2_first_freq('input-part1.txt'))
