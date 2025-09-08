from array import array

numbers = array('i', [1, 2, 3, 4, 5])

print("Original array:", numbers.tolist())

numbers.append(6)
print("After appending 6:", numbers.tolist())

numbers.remove(3)
print("After removing 3:", numbers.tolist())

print("Element at index 2:", numbers[2])

numbers.pop()
print("After popping last element:", numbers.tolist())

numbers.reverse()
print("After reversing the array:", numbers.tolist())

numbers.buffer_info()
print("Buffer info (address, length):", numbers.buffer_info())

numbers.typecode
print("Type code of the array:", numbers.typecode)