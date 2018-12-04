from collections import defaultdict

def read_file(filename):
	with open(filename) as f:
		return [x.strip() for x in f.readlines()]

def get_overlap_claims(claims):

	claim_grid = {}
	tot_overlaps = 0 
	for claim in claims:
		claimid, _, edgedists, area = claim.split()
		leftedge, topedge = map(int,edgedists.strip(':').split(','))

		width, height = map(int, area.split('x'))
		#print(leftedge, topedge, width, height)
		for j in range(topedge, topedge+height):
			for i in range(leftedge, leftedge+width):

				claim_grid[(i,j)]= claim_grid.get((i,j),0) + 1
				
	
	return sum(x > 1 for x in claim_grid.values())



def get_nonoverlap_claim(claims):

	claim_grid = {}
	claimid_store = defaultdict(list)
	tot_overlaps = 0 
	for claim in claims:
		claimid, _, edgedists, area = claim.split()
		leftedge, topedge = map(int,edgedists.strip(':').split(','))

		width, height = map(int, area.split('x'))
		
		for j in range(topedge, topedge+height):
			for i in range(leftedge, leftedge+width):
				
				claim_grid[(i,j)] = claim_grid.get((i,j),0) + 1
				claimid_store[claimid].append((i,j))
				

	for clamid, claimpoints in claimid_store.items():
		if all(claim_grid[point] == 1 for point in claimpoints):
			return clamid
		

sample_claims = ['#1 @ 1,3: 4x4',
		  '#2 @ 3,1: 4x4',
		  '#3 @ 5,5: 2x2']


claims = read_file('day3-input.txt')

print(get_overlap_claims(claims))
print(get_nonoverlap_claim(claims))


