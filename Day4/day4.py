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
	gaurd_sleep_times = defaultdict(list)
	gaurd = None
	sleep = True
	for note in notes:
		if re.search(r'[0-9]+', note[1]):
			gaurd = re.findall(r'[0-9]+', note[1])[0]
		elif note[1].lower() == 'falls asleep':
			sleep_time = note[0]
		elif note[1].lower() == 'wakes up':
			wakeup_time = note[0]
			tot_sleep_time = (wakeup_time - sleep_time).total_seconds() // 60
			gaurd_sleep_times[gaurd].append(tot_sleep_time)

	







if __name__ == "__main__":
	notes = read_file('day4-sample-input.txt')
	print("*********Before Sort********")
	print_notes(notes)
	notes =  sort_notes(notes)
	print("*********After Sort********")
	print_notes(notes)



