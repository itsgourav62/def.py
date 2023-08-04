#Python program to convert time seconds in hours, minutes, seconds
seconds= int(input("Enter time in Sec:"))
hour=seconds//3600
seconds%= 3600
min =seconds//60
seconds%=60
print(hour,"hr,",min,"minutes,",seconds,"sec")