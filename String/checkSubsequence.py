# Python Implementation of the approach
import itertools

def Sub_Sequences(Stri):
	combs = []
	for l in range(1, len(Stri)+1):
		combs.append(list(itertools.combinations(Stri, l)))
	for c in combs:
		for t in c:
			print (''.join(t), end =' ')

# Testing with driver code
if __name__ == '__main__':
	Sub_Sequences('abc')
