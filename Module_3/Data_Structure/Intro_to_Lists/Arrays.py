'''
In Python, Array is just a ordered homogenous elements. Python arrays are just wrappers for C Arrays.
The Type of Arrays are constrained and specified at the time of creation.
'''
# Intializing Arrays 
import array
new_array = array.array('f', [1,2,4])  # f means data type is Float
print(new_array[0])
'''
There are several types of arrays in Python; refer to the table below for a complete list.

Type code        C Type          Python Type       Minimum Size in Bytes
'c'             character           char                   1
'b'             signed char         int                    1
'B'             unsigned char       int                    1
'u'              Py_UNICODE     Unicode character     2 or 4 depending on Unicode build
'h'              signed short       int                    2
'H'             unsigned short      int                    2
'i'              signed int         int                    2
'I'              unsigned int       long                   4
'l'             signed long         int                    4
'L'            unsigned long        long                   4
'f'               float             float                  4
'd'               double            float                  8
'''
# Array Slicing:
'''
Array Slicing is done as same way list slicing is done.
'''


initializer_list = [2, 5, 43, 5, 10, 52, 29, 5]
number_array = array.array('i', initializer_list)

print(number_array[1:5])  # 2nd to 5th
print(number_array[:-5])  # beginning to 3rd
print(number_array[5:])  # 6th to end
print(number_array[:])   # beginning to end

# Changing or Adding Array Elements
integers = array.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
integers[0] = 0
print(integers)  # array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
integers[2:5] = array.array('i', [4, 6, 8])
print(integers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

# To add one element into array we use append()
integers.append(15)
print(integers)
# To add multiple elements into array we can use extend() method
integers.extend([17,19,35])
print(integers)

# Concatenation of arrays using '+'
odd = array.array('i',[1,3,5,7])
even = array.array('i', [0,2,4,8])
integ = array.array('i') # creating empty array
integ = odd + even
print(integ)

# Removing/ del elemnts: We use remove(value) method to remove a value(It removes the first value that comes ==value)
# We use del statement to remove multiple of all of array 
# We use pop(index) method to remove an elemnt at that index in array(If index is not found or element is not found gives error)

print(integ.remove(7)) # removing elements from array using remove() 
print(integ)
print(integ.pop(2))    # removing elemnts from array with given index using index()
print(integ)
# Removing muliple elements from array using del statement
del integ[2:5]
print(integ)


