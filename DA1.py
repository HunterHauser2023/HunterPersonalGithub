import math

#variables used in the code 
numMean = 0
variance = 0
smallestNum = 89.4
largestNum = 0
floatNum = [24.3, 32.5, 34.5, 66.7, 17.4, 30.5, 55.4, 11.5, 10.3, 0.4, 31.9, 89.4, 33.2, 75.2, 43.6]

#counts the amount of values in the list
print("Count of the numbers:", len(floatNum))


#goes through floatNum and adds all the values then divides by length
for i in floatNum:
	numMean = numMean + i
	totalMean = numMean/len(floatNum)

print( "Average(mean) of the numbers:", "{:.2f}".format(totalMean))

#calculates variance used in standard deviation by founding difference of each value from mean
for i in floatNum:
	variance = variance + (i - totalMean)**2

#calculates standard deviation 
standardDev = math.sqrt(variance/len(floatNum))
print("Standard Deviation of the numbers","{:.2f}".format(standardDev))

#sorts the numbers from smallest to biggest 
floatNum.sort()

#prints middle indexed value
for i in floatNum[7:8]:
	print("Median:", i)

#compares each value in floatNum to previous value to find smallest/largest number
for i in floatNum:
	if (smallestNum  > i ):
		smallestNum = i
	elif(largestNum < i ):
		largestNum = i


print("Smallest Number:","{:.2f}".format(smallestNum))
print("Largest Number:","{:.2f}".format(largestNum))

#allows user to index and replace a point 
user_index = input("Please enter a number from 0-14 to index a point: ")
userNum = input("Please enter a number to put in the indexed position (x.x): ")

user_index = int(user_index)
userNum = float(userNum)

#puts users indexed point in value in floatNum and replaces previous value
floatNum[user_index] = userNum

print("\n", floatNum)

#rverses the list and prints with _
for i in floatNum[:0:-1]:
		print(i, end="_ ")
print(floatNum[0])


print("\n")

