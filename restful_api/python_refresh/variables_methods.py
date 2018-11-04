# Variables
a = 2
b = 'words'

print(a)
print(b)


# Methods
def my_print_method(my_argument):
	print(my_argument)

my_print_method("Hello, World!")


# list, tuples, sets
# list
grades = [77, 88, 90, 95, 100]
print(sum(grades) / len(grades))

# tuples: immutable, cant increase the size
tuples_grades = (77, 88, 90, 95, 100)

tuples_grades = tuples_grades + (99,) # add to a tuple

# sets: Unique & unordered
set_grades = {77,80,90,100,100}

## Set Operations
your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}
print(your_lottery_numbers.intersection(winning_numbers)) # union, difference, intersection


# for loops: iterates to the length of the list for each element
# character is a variable to keep track...each element of the iterable
# my_string >> iterables: Lists, sets, tuples, and more
my_variable = "hello"

for character in my_variable: 
	print(character)

my_list = [1,3,5,7,9]

for number in my_list:
	print(number ** 2)

# While loops
user_wants_number = True 
while user_wants_number == True:
	print(10)
	
	user_input = input("Should we print again? (y/n)")
	if user_input == 'n':
		user_wants_number = False


# If Statements
should_continue = True
if should_continue:
	print("hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in known_people:
	print("you know {}!".format(person))
else:
	print("you don't know {}!".format(person))


# Flow Control
numbers = [1,2,3,4,5,6,7,8]

def even_numbers(numbers):
    evens = []
    for element in numbers:
        if element % 2 == 0:
            evens.append(element)
    return evens


# Pass
# a way to just pass


# List comprehension
# Build list programmaticly

my_list = [0,1,2,3,4,5]

multiply_list = [x*3 for x in range(5)]
print(multiply_list)

print([n for n in range(10) if n % 2 == 0]) 

people_you_know = ["John", "Michael", "Jeff"]
normalized_people = [person.strip().lower() for person in preson_you_know]


# Dictionaries
universities = [
	{
		'name': 'Oxford'
		'location': 'UK'
	},
	{
		'name': 'MIT'
		'location': 'US'	
	}
]

# Classes & Objects
class LotteryPlayer:
	def __init__(self, name):
		self.name = name,
		self.numbers = (5,,9,12,3,1,21)

	def total(self):
		return sum(self.numbers)

player_one = LotteryPlayer("Kevin")


# Classmethod and staticmethod
# Differences in what we pass to methods
@classmethod 
def go_to_school(cls)
	print("I'm going to school")

@staticmethod
def go_to_school()
	print("I'm going to school")


# Inheritance


# args & kwargs 
# args pass into a list
# kwargs passs into a set
def addition_simplified(*args):
	return sum(args)

addition_simplified(1,3,4,5,6,62)

def what_are_kwargs(*args, **kwargs)
	print(args)
	print(kwargs)

what_are_kwargs(12,35,66, name='Jose', location='UK')


# Passing functions as parameters
# lambda function
def methodception(another):
	return another()

print(methodception(lambda: 35+77))

my_list = [1,2,3,4,5,6,7,8]
print(list(filter (lambda x: x != 2, my_list) ))

# identical
############################
(lambda x: x * 3)(5)

def f(x):
	return x * 3
f(5)
############################

# decorators
# function that gets called before another function
# Extends a function
# decorator should always call the function
import functools

def my_decorator(func)
	@functools.wraps(func)
	def function_that_runs_fun():
		print("In the decorator!")
		func()
		print("After the decorator!")
	return function_that_runs_func

@my_decorator
def my_function():
	print("I'm the function!")

# Advanced Decorators
# 3 levels of functions

def decorator_with_arguments(number):
	def my_decorator(func):
		@functools.wraps(func)
		def function_that_runs_func(*args,**kwargs):
			print("In the decorator!")
			if number == 56:
				print("Not running the function!")
			else:
				func(*args,**kwargs)
			print("After the decorator!")
		return function_that_runs_func
	return my_decorator

@decorator_with_arguments
def my_function_too(x,y)
	print(x+y)

my_function_too(57,67)
