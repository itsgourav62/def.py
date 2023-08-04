# Python program to check
# if a string is binary or not

def check(string) :


	p = set(string)
	s = {'0', '1'}
	if s == p or p == {'0'} or p == {'1'}:
		print("True")
	else :
		print("False")


		
# driver code
if __name__ == "__main__" :

	string = "10101111"

	
	check(string)
