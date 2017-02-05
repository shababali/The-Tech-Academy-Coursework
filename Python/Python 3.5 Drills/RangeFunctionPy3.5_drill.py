# Python: 3.6.0
# Tech Academy Python Drill - Learning the Range Function.


# Example
my_list = ['one', 'two', 'three', 'four', 'five']
my_list_len = len(my_list)
for i in range(0, my_list_len):
    print(my_list[i])
print('')

# range([start], [stop], [step]) ie range function has 3 parameters.
#       [start] - starting from number...
#       [stop] - stopping before number...
#       [step] -  ‘count by’ number...
#   ie range(10,0,-4)==[10,6,2]



''' 1. Start IDLE and use the Python range() function with one parameter to display the
following:
0
1
2
3
'''
print('DRILL 1')
my_list1 = [0,1,2,3]
my_list1_len = len(my_list1)
for i in range(0, 4, 1):
    print(my_list1[i])
print('')


for i in range(0, 4, 1):
    print(i)
print('')

for i in range(4): # Soultion to the question, default start and step arguments are passed in for the parameters.
    print(i)
print('')




'''2. Use the Python range() function with 3 parameters to display the following:
3
2
1
0'''
print('DRILL 2')
my_list2 = [3,2,1,0]
my_list2_len = len(my_list2)
for i in range(0, 4, 1):
    print(my_list2[i])
print('')


for i in range(3, -1, -1):
    print(i)
print('')


'''3. Use the Python range() function with 3 parameters to display the following:
8
6
4
2
'''
print('DRILL 3')
my_list3 = [8,6,4,2]
my_list3_len = len(my_list3)
for i in range(0, 4, 1):
    print(my_list3[i])
print('')


for i in range(8, 0, -2):
    print(i)
print('')

