import time
import random
import heapq

implemented = []
#The various sorting algorithms. I've tried to use the simplest implementations for study purposes.

def bubble_sort(bad_list):
	sorted = False
	i = 0
	while not sorted:
		sorted = True
		print("Each time we go through the array, we will assume it's already sorted until we find an element out of place.")
		for n in range(len(bad_list)-1):
			if bad_list[n] > bad_list[n+1]:
				sorted = False
				print ("Need to swap: " , bad_list[n], "is greater than ", bad_list[n+1])
				bad_list[n], bad_list[n+1] = swap(bad_list[n], bad_list[n+1])
				print ("Swapped:", bad_list[n], bad_list[n+1])
			else:
				print(bad_list[n])
		print ("Now the array looks like this: \n", bad_list)
	return bad_list

def selection_sort(bad_list):
	for i in range(len(bad_list)):
		curr_min = min(bad_list[i:])
		mindex = bad_list[i:].index(curr_min)
		bad_list[i + mindex] = bad_list[i]
		bad_list[i] = curr_min #no function call necessary
		print(bad_list)
	return bad_list
			
def insertion_sort(bad_list):
	for i in range(1, len(bad_list) - 1):
		x = bad_list[i]
		j = i 
		while j > 0 and bad_list[j-1] > x:
			bad_list[j] = bad_list[j-1]
			j -= 1
		bad_list[j] = x
		print(bad_list)
	return bad_list


'''
def merge_sort(bad_list):
	print "Coming soon"

def shell_sort(bad_list):
	print "Coming soon"
'''

def heap_sort(bad_list):
	#Note that we are using python's native min heap instead of the max heap used in textbooks. Maybe I'll write a max heap for python at some future date.
	h= []
	for val in bad_list:
		heapq.heappush(h, val)
		print(h)
	return [heapq.heappop(h) for i in range(len(h))]

#Utility functions used by the various algorithms. Allegedly, good practice is "If you use it more than twice, put it in a function"
def swap(a, b):
	#Using local variables to swap the actual contents instead of references.
	localA, localB = b, a
	return localA, localB
	
print("This script is designed to illustrate various sorting algorithms that Ysoschor Fried \n asked me about while studying for a final exam in data structures.")
time.sleep(0.75)

funcs = [bubble_sort, selection_sort, insertion_sort, heap_sort]

while True:
	print("A loop generates a bunch of random integers 0 <= N <= 500 to be sorted. \n\n")
	a = random.sample(range(0, 500), 10)
	aString = ', '.join(map(str, a)) 
	print (aString)
	print ("\n\nThis script generates a new array each time you want to try out a new algorithm.")
	print("\nThe following Sorts have been illustrated so far. Enter the number of the sort you wish to watch: \n")
	for i in range(len(funcs)):
		print (i, "\t", str(funcs[i]))
	call = input("Call a func by number: ")
	try:
		int(call)
		print ("You called function ", call, "\n\n")
		b = funcs[int(call)](a)
	except:
		print (call, " has not been implemented yet, or is an invalid input. \nInput is valid if and only if it is a number from the left column in the above list.")
		print ("Try again.")
		time.sleep(0.5)
	pass