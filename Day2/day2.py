from collections import Counter

def read_file(filename):
	with open(filename) as f:
		return [x.strip() for x in f.readlines()]

def calcchecksum(idlist):
	twoletter_ids = threeletter_ids = 0
	for idpkg in idlist:
		two_counted = three_counted = False
		id_counter = Counter(idpkg)
		for k,v in id_counter.items():
			if v == 2 and not two_counted:
				twoletter_ids += 1
				two_counted = True
			if v == 3 and not three_counted:
				threeletter_ids += 1
				three_counted = True

	return threeletter_ids * twoletter_ids


def oddchars(s1, s2):
	i = 0
	onechange = False
	oddchars = ""
	oddpos = -1
	while i < len(s1):
		if s1[i] != s2[i]:
			if onechange:
				return ""
			else:
				oddchars = s1[i]+s2[i]
				oddpos = i
				onechange = True
		i += 1

	return s1[:oddpos] + s2[oddpos+1:] if oddpos >= 0  else ""




def findidenticalids(idlist):
	chars = ""
	for i in range(len(idlist)):
		for j in range(i+1, len(idlist)):
			if len(idlist[i]) != len(idlist[j]):
				continue
			else:
				chars += oddchars(idlist[i], idlist[j])

	return chars
				

if __name__ == "__main__":
	idlist = read_file('part2-input.txt')
	print(calcchecksum(idlist))
	print(findidenticalids(idlist))
