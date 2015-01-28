import time
import random
implemented = []
#The various sorting algorithms. I've tried to use the simplest implementations for study purposes.

def bubbleSort(bad_list):
	sorted = False
	i = 0
	while not sorted:
		sorted = True
		print sorted
		print "Each time we go through the array, we will assume it's already sorted until we find an element out of place."
		for n in range(len(bad_list)-1):
			if bad_list[n] > bad_list[n+1]:
				sorted = False
				print ("Need to swap: " , bad_list[n], "is greater than ", bad_list[n+1])
				bad_list[n], bad_list[n+1] = swap(bad_list[n], bad_list[n+1])
				print ("Swapped:", bad_list[n], bad_list[n+1])
			else:
				print bad_list[n]
		print "Now the array looks like this: \n", bad_list
	return bad_list

def selectionSort(bad_list):

	for i in range(len(bad_list)):
		curr_min = min(bad_list[i:])
		mindex = bad_list[i:].index(curr_min)
		bad_list[i + mindex] = bad_list[i]
		bad_list[i] = curr_min #no function call necessary
		print bad_list
		'''
	source = [4,2,1,10,5,3,100]
	for i in range(len(source)):
		mini = min(source[i:]) #find minimum element
		min_index = source[i:].index(mini) #find index of minimum element
		source[i + min_index] = source[i] #replace element at min_index with first element
		source[i] = mini                  #replace first element with min element
	print source
		'''
	return bad_list
			
def insertionSort(bad_list):
	for i in range(1, len(bad_list) - 1):
		x = bad_list[i]
		j = i 
		while j > 0 and bad_list[j-1] > x:
			bad_list[j] = bad_list[j-1]
			j -= 1
		bad_list[j] = x
		print bad_list
	return bad_list


#Utility functions used by the various algorithms. Allegedly, good practice is "If you use it more than twice, put it in a function"
def swap(a, b):
	#Using local variables to swap the actual contents instead of references.
	localA, localB = b, a
	return localA, localB
	
print "Hello Wrold! \n\n"
time.sleep(0.75)
print "This script is designed to illustrate various sorting algorithms that Ysoschor Fried \n asked me about while studying for a final exam in data structures."
time.sleep(0.75)
print "It is also designed to allow me to play with Python.\n"
time.sleep(0.75)

funcs = [bubbleSort, selectionSort, insertionSort]

while True:
	print "A loop generates a bunch of random integers 0 <= N <= 500 to be sorted. \n\n"
	a = random.sample(range(0, 500), 10)
	aString = ', '.join(map(str, a)) 
	print aString
	print "\n\n This script generates a new array each time you want to try out a new algorithm."
	print"\n The following Sorts have been illustrated so far. Enter the number of the sort you wish to watch: \n"
	for i in range(len(funcs)):
		print i, "\t", str(funcs[i])
	call = input("Call a func by number: ")
	try:
		int(call)
		print "You called function ", call
		b = funcs[int(call)](a)
	except:
		print call, " has not been implemented yet, or is an invalid input. \nInput is valid if and only if it is a number from the left column in the above list."
		print "Try again."
		time.sleep(0.5)
	pass