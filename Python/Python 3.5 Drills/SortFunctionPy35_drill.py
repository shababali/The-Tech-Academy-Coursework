# Python: 3.5.1
# Tech Academy Python Drill - Learning the Sort Function.

'''DRILL:

Write your own version of the sorted() method in Python. This method should take a list as an argument and return a list that is sorted in ascending order. Call your method passing in the following lists as arguments and print out each sorted list to the shell. This should be an algorithm that you write. Do not use .sort() or the sorted() methods in your method.

[67, 45, 2, 13, 1, 998]

[89, 23, 33, 45, 10, 12, 45, 45, 45]

Your sorted lists should look like this when displayed:

[1, 2, 13, 45, 67, 998]

[10, 12, 23, 33, 45, 45, 45, 45, 89]

Your specific algorithm does not need to match the solution your Instructor has. It simply needs to work.'''


# Before Sort
listA = [67,45,2,13,1,998]
listB = [89,23,33,45,10,12,45,45,45]
print(listA)
print('')
print (listB)
print ('')
print('After Selection Sort Function Implementation:')
print ('')

# After Sort

def selectionSort(listX):
    #1. Outer for loop establishes the number of passes through the unsorted array and mutually fills a hypothetical sorted array
    #    by filling the sorted array end with a pass determined Max value.  
    #    The number of passes will equal (unsorted array length - 1), as the penultimate pass automatically places the
    #    sorted array's minimum value into the first spot.
    #1. Each pass will incrimentally reduce the diminishing unsorted array list length by one value:
          # because the Max value of any pass is taken from the unsorted array instance,
          # and filled into the corresponding terminal slot of a hypothetical sorted array instance.
          # For example, Pass 1: will take Max val in (unsorted array length) and fill slot (sorted array length).
          #              Pass 2: will take Max val in (unsorted array length - 1) and fill slot (sorted array length - 1)
          
          #Function Demo: Array with 6 values will have 5 passes:
          #                Pass 1 will read through 6 values in unsorted array and place Max val into into sorted array slot #6.
          #                Pass 2 will read through 5 values in unsorted array and place Max val into into sorted array slot #5.
          #                Pass 3 will read through 4 values in unsorted array and place Max val into into sorted array slot #4.
          #                Pass 4 will read through 3 values in unsorted array and place Max val into into sorted array slot #3.
          #                Pass 5 will read through 2 values in unsorted array and place Max val into into sorted array slot #2.
          #                slot #1 is filled in automatically as a result of the 5 passes.
          
   
    # 2. Each pass will evaluate 1 fewer unsorted array values as the Max value 
 
   for fillslot in range(len(listX)-1,0,-1): #1 Passes through unsorted array:  
       positionOfMax=0                       #  since the count is diminishing - the hypothetical sorted array is being filled with a respective passes' Max value at the terminal slot, ie positionOfMax = 0.
       for location in range(1,fillslot+1):  
           if listX[location]>listX[positionOfMax]: #Inner for loop iterates through the values inside the diminshing unsorted array   
               positionOfMax = location             # Per pass - the hypothetical sorted array terminal slot exchanges values if the iteration encounters a greater value elsewhere in the unsorted array.

       temp = listX[fillslot]
       listX[fillslot] = listX[positionOfMax]   # Values are filled into the hypothetical sorted array slot by exchange with the unsorted array through the variable 'temp'.
       listX[positionOfMax] = temp


listA = [67,45,2,13,1,998]
listB = [89,23,33,45,10,12,45,45,45]
selectionSort(listA)
selectionSort(listB)
print(listA)
print('')
print (listB)




# Effectively the selection sort goes through the values from left to right
# and sorts them by moving the largest value to the right and then performing
# another pass, but ignoring that rightmost position as it is already set.  It
# keeps passing until all of the values are in order of smallest to largest value.
