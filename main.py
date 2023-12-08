from loops import *
from recursion import *

print('Factorial of 6 using a loop is', loops.factorial(6))
print('Factorial of 5 using a loop is', loops.factorial(5))
print('Factorial of 1 using a loop is', loops.factorial(1))

print('Factorial of 6 using recursion is', recursion.factorial(6))
print('Factorial of 5 using recursion is', recursion.factorial(5))
print('Factorial of 1 using recursion is', recursion.factorial(1))


print ('2 to the 5th power using a loop is', loops.power(2,5))
print ('2 to the 4th power using a loop is', loops.power(2,4))
print ('2 to the 0 power using a loop is', loops.power(2,0))

print ('2 to the 5th power using recursion is', recursion.power(2,5))
print ('2 to the 4th power using recursion is', recursion.power(2,4))
print ('2 to the 0 power using a recursion is', recursion.power(2,0))

nums = [5,12,3,4]
print("Minimum number using a loop is", loops.computeMin(nums))
print("Minimum number using recursion is", recursion.computeMin(nums, 0, nums[0]))

str = 'CAT'
loops.reverse(str)
recursion.reverse(str, len(str))


numbers = -7, 42, 70, 39, 3, 63, 8
startingindex = 0
listsize = 7
target= 39

numbers = input('Enter seven numbers separated by a space')
startingindex = input('Enter index at which the search will begin')
listsize = input('Enter size of list that will be searched')
target = input('Enter the target value to search for')
print(recursion.search(numbers, startingindex, listsize, target, 0, False))