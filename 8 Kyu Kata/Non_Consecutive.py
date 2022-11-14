# Code by Tajrina Promela
# Date 17th September 2022, 5:02 PM
# Program to find the first Non-Consecutive number in Python

numbers = []

def non_consecutive(numbers):
    for i, j in enumerate(numbers, numbers[0]): # Two counter variables
        # i is the placeholder and j is the list item
        print("i is: " + str(i) + ", j is: " + str(j))
        if i != j: # Comparing whether the list is sequential or not
            return j

'''size = int(input("Enter the size of the array: "))
print("Enter the elements of the array: ")
nums = []

for i in range(size):
    n = int(input())
    nums.append(n)

print("The Non-Consecutive integer is: " + str(non_consecutive(nums)))'''

print(non_consecutive([1,2,3,4,6,7,8]))