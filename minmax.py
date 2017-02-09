 			
#this code finds the min and max values using for loop
def find_minmax(n):
	max = min = a[1]
	for (i = 2 to n):  #assumes the first item in the array is min and max
 	#then it checks the second value in array and loops through to n

 		#if value in next array is geater than the current, max now becomes the value in next array
 		if  (a[1]>max):
 			then max = a[1]
 			#does the same for min and loops through the entire array 
 		else if (a[1]<min):
 			then min = a[1]
 			print ('min,max')

 	