#Write a program to convert a number entered by the user into its corresponding number in words. 
#for example if the input is 876 then the output should be ‘Eight Seven Six

n = input ("Enter a number = ")
dic = { "0" : "Zero" , "1":"One " , "2" : "Two" , "3" : "Three" , "4" : "Four" , "5" : "Five" , "6" : "Six" , "7" : "Seven" , "8" : "Eight" , "9" : "Nine"}

for i in n :
    print( dic[i], end = " ")