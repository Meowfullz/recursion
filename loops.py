class loops:
	@staticmethod
	def factorial(n:int):
		"""Computes the factorial of a specified number.
	
		Args:
			n (int): specified number; for example, 6

		Returns:
			int: Computed factorial
	"""
		
		# the counter variable i more or less contains the
		# same value as the parameter n

		# the loop will repeat as long as i > 1
		#the condition that will cause the loop to stop
		# is when i == 1 -> stopping case for the loop
		i = n - 1
		while (i > 1):
			n = n * i
			# n = 6 * 5
			# n = 30 * 4
			#n = 120 * 3
			#n = 360 * 2
			i = i - 1

		return n
	
	@staticmethod
	def power(number: int, power:int):
		"""Takes a specified number to a specified power

		Args:
			number (int): specified number for example 2
			power (int): specified number for example 5

		Returns:
			int: computed power
		"""
		# the counter variable for the loop contains the
		# same value as power

		# the loop will repeat as long as i>1
		# the condition that will cause the loop to stop
		# is when i == 1 -> stopping case for the loop

		# with each iteration of the loop, we're decrementing
		# the counter variable by 1
		result = 1

		i = power
		while (i>0):
			result = result * number
			# result = 1 * 2
			i = i - 1

		return result
	
	@staticmethod
	def computeMin(nums):
		"""Finds the minimum number in a specified list of numbers
		

		Args:
			nums: specified list

		Returns:
			int: minimum number
		"""

		# the counter variable of the loop is the 
		# index used to iterate through the elements in the list 

		# the loop will repeat as long as i < len(nums
		# the condition that will cause the loop to stop
		# is i == len(nums) -> stopping case for the loop

		# with each iteration of the loop we're incrementing
		# the counter variable by 1

		# when the loop stops, it returns min

		i = 0
		min = nums[i]

		while (i < len(nums)):
			if (nums[i] <= min):
				min = nums[i]
			i += 1
		
		return min
	
	@staticmethod
	def reverse(s:str):
		"""displays a specified string in reverse

		Args:
			s (str): specified str
		"""

		# the counter variable in the loop is the index
		# used to iterate through the characters in the string

		# the stopping case for the loop is i == 0

		# with each iteration of the loop, we're 
		# decrementing the counter variable

		 # when the loop stops, we're printing a message
		i = len(s)
		while (i > 0):
			print(s[i-1], end='')
			i -= 1
		print(' is the reverse of %s using a loop' % (s))