# Python program to execute
# time of a program

# importing time module
from time import time
class Timer:

	def __init__(self, func):
		self.function = func

	def __call__(self, *args, **kwargs):
		start_time = time()
		print("Before triggering the function i am using while loop")
		i=0
		while i<=5:
			i=i+1

			result = self.function(*args, **kwargs)

		end_time = time()
		print("Execution took {} seconds".format(end_time-start_time))
		return result


# adding a decorator to the function
@Timer
def some_function(delay):
	from time import sleep

	# Introducing some time delay to
	# simulate a time taking function.
	sleep(delay)

some_function(3)

