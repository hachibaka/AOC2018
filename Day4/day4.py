import datetime
import re
from collections import defaultdict

def read_file(filename):
	gaurd_notes = []
	with open(filename) as f:
		for line in f.readlines():
			tsendpos = line.find(']')
			timestamp = datetime.datetime.strptime(line[1:tsendpos], "%Y-%m-%d %H:%M")
			note = line[tsendpos+2:]
			gaurd_notes.append((timestamp, note.strip()))

	return gaurd_notes

def sort_notes(notes):
	return sorted(notes, key=lambda x: x[0])

def print_notes(notes):
	for note in notes:
		print(note)

def parse_notes(notes):
	gaurd_sleep_times = {}
	
	gaurd = None
	
	for note in notes:
		if re.search(r'[0-9]+', note[1]):
			gaurd = int(re.findall(r'[0-9]+', note[1])[0])
		elif note[1].lower() == 'falls asleep':
			sleep_time = note[0].minute
		elif note[1].lower() == 'wakes up':
			wakeup_time = note[0].minute
			if gaurd in gaurd_sleep_times:
				for i in range(sleep_time, wakeup_time):
					gaurd_sleep_times[gaurd][i] += 1
			else:
				gaurd_sleep_times[gaurd] = [0 for _ in range(60)]
				for i in range(sleep_time, wakeup_time):
					gaurd_sleep_times[gaurd][i] += 1

	return gaurd_sleep_times

def calc_part1(gaurd_sleep_times):
	maxsleep = -1
	maxgaurd = None
	for gaurd in gaurd_sleep_times.keys():
		sleepsum  = sum(gaurd_sleep_times[gaurd])
		
		
		if maxsleep < sleepsum:
			maxsleep = sleepsum
			maxgaurd = gaurd

	maxminute = gaurd_sleep_times[maxgaurd].index(max(gaurd_sleep_times[maxgaurd]))
	print(maxminute, maxgaurd, maxgaurd * maxminute)
	return maxgaurd * maxminute

def calc_part2(gaurd_sleep_times):
	maxsleep = -1
	maxgaurd = None
	for gaurd in gaurd_sleep_times.keys():
		sleepmax  = max(gaurd_sleep_times[gaurd])
		
		
		if maxsleep < sleepmax:
			maxsleep = sleepmax
			maxgaurd = gaurd

	maxminute = gaurd_sleep_times[maxgaurd].index(max(gaurd_sleep_times[maxgaurd]))
	print(maxminute, maxgaurd, maxgaurd * maxminute)
	return maxgaurd * maxminute


if __name__ == "__main__":
	notes = read_file('day4-input.txt')
	print("*********Before Sort********")
	print_notes(notes)
	notes =  sort_notes(notes)
	print("*********After Sort********")
	print_notes(notes)
	gaurd_sleep_times = parse_notes(notes)
	print(gaurd_sleep_times)
	print("part 1 - ID multiplied by minute is ", calc_part1(gaurd_sleep_times))
	print("part 2 - ID multiplied by minute is ", calc_part2(gaurd_sleep_times))



