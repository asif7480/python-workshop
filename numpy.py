# numpy workout
import numpy as np
# NumPy (Numerical Python) is a Python library used to work with numerical data.
# NumPy includes functions and data structures that can perform a wide variety of mathematical operations.
# In Python, lists are used to store data.
# NumPy provides an array structure for performing operations with data.
# NumPy arrays are faster and more compact than lists.
# for example
# ----------------------

# x = np.array([1,2,3,4])
# print(x[2])

# ----------------------


# NumPy arrays are often called ndarrays, which stands for "N-dimensional array", because they can have multiple dimensions.
# for example

# ----------------------
# x=np.array(
#     [
#         [2,4,6,8],
#         [3,6,9,12],
#         [4,8,12,16]
#     ])
# print(x[2][2])
# ----------------------

# This will create a 2-dimensional array, which has 3 columns and 3 rows, and output the value at the 2nd row and 3rd column.

# Arrays have properties, which can be accessed using a dot.
# ndim returns the number of dimensions of the array.
# size returns the total number of elements of the array.
# shape returns a tuple of integers that indicate the number of elements stored along each dimension of the array.
# for example

# -----------------------------------------------------------------------------
# print('dimension of array is: ', x.ndim)
# print('size of array is:', x.size)
# print('shape of array is: ',x.shape, "\nHere the shape is basically a tuple")
# -----------------------------------------------------------------------------

# # -----------------------------------------------------------------------------
# # We can add, remove and sort an array using the np.append(), np.delete() and np.sort() functions.
# x= np.array([6,2,4])
# # add an element
# x = np.append(x,5)
# print("added an element in the last index using append method", x)
# # delete at index
# x = np.delete(x, 0)
# print("Deleted value of zero index", x)
# # sort the array
# x = np.sort(x)
# print("Sort the array using sort method: ", x)

# # -----------------------------------------------------------------------------

# #
# # np.arange() allows you to create an array that contains a range of evenly spaced intervals (similar to a Python range)
# y = np.arange(0, 12)
# print(y)

# # This is a 1-dimensional array, containing 12 elements.

# # NumPy allows us to change the shape of our arrays using the reshape() function. For example, we can change our 1-dimensional array to an array with 4 rows and 3 columns:
# reshape_arr = y.reshape(4,3)
# print(reshape_arr)

# # Reshape can also do the opposite: take a 2-dimensional array and make a 1-dimensional array from it:

# simple_arr = np.array([ [1,2], [3,4], [5,6] ])
# simple_to_reshape = simple_arr.reshape(6)
# print(simple_to_reshape)  


# indexing and slicing
arr = np.arange(0,11,2)
# print("arr value from 0 to 10: ",arr)
# print("arr[0:2] means array from 0 index to excluding 2 index: ",arr[0:2])
# print(arr[5:])
# print(arr[:4])
print(arr[-3:])
print(arr[:-3])


# condtitionals
arr = np.arange(0,11)
print("arr[arr<4] will only print value less than 4: ", arr[arr<4])
print("arr[arr>4] will only print value greater than 4: ", arr[arr>4])
print("arr[arr==4] will only print value equal to 4: ", arr[arr==4])
print("arr[arr!=4] will only print value not equal to 4: ", arr[arr!=4])

print("value greater than 4 and divisible by 2: ", arr[ (arr>4) & (arr%2==0) ])

# operations
print(arr.sum())
print(arr.min())
print(arr.max())
arr_multiplyBy_two = arr*2
print(arr_multiplyBy_two)

# calculating mean, median, standard deviation, variance
print("Mean", np.mean(arr_multiplyBy_two))
print("Median", np.median(arr_multiplyBy_two))
print("standard deviation", np.std(arr_multiplyBy_two))
print("Variance", np.var(arr_multiplyBy_two))