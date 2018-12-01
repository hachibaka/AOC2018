import bisect
from itertools import accumulate, cycle
import time

def part1_tot_freq(freqchanges):
	return sum(freqchanges)


def part2_first_freq(freqchanges):
	seenfreq = [0]
	start = 0
	
			
	
	maxindex = len(freqchanges)
	print("Length of list is ",maxindex)
	listloopcounter = i = 0
	while True:
		if i == maxindex:
			i = 0
			listloopcounter +=1
			#print("Number of time list has been looped is {} and start is {}".format(listloopcounter,start))
		start += freqchanges[i]
		i+=1
		position = bisect.bisect(seenfreq, start)
		if seenfreq[position-1] == start:
			return start
		else:
			bisect.insort(seenfreq, start)
			
#Copied from Reddit user, seems to be fast.
def part2_first_freq_set(freqchanges):
	seen = {0}
	return next(f for f in accumulate(cycle(freqchanges)) if f in seen or seen.add(f))


def read_file(filename):
	with open(filename) as f:
		return [int(x.strip()) for x in f.readlines()]

if __name__ == "__main__":
	freqchanges = read_file('input-part1.txt')
	print("total sum of frequency is ",part1_tot_freq(freqchanges))
	start_time = time.time()
	print("First frequency seen twice is ",part2_first_freq(freqchanges))
	print("Total time taken for finding duplicate using bisect is ", time.time() - start_time)
	start_time = time.time()
	print("First frequency seen twice is ",part2_first_freq_set(freqchanges))
	print("Total time taken for finding duplicate using set is ", time.time() - start_time)