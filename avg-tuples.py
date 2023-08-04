#Write a Python program to calculate the average value of the numbers in a given tuple of tuples.

def average_tuple(num):
    avg = tuple(map(lambda x: sum(x) / float(len(x)), zip(*num)))
    return avg

num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\nAverage value of the numbers in tuple of tuples:\n",average_tuple(num))
num = ((10, 20, 30), (40, -50, 60), (70, -80, 90))
print("\nAverage value of the numbers in tuple of tuples:\n",average_tuple(num))


