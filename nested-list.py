#Get the first element from each nested list in a list


def Extract(lst):
	return [item[0] for item in lst]
	
lst = [[0, 1, 4], [1, 3], [2, 7, 8]]
print(Extract(lst))
