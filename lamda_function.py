#Even or odd
even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even(8))
print(even(5))

#Sort a list
students = [("Ram", 85), ("Shyam", 70), ("Sita", 95)]
students.sort(key=lambda x: x[1])
print("Sorted list: ",students)

#Find the square of each elements in a list using map() function
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*x, numbers))
print("Square of each elements: ",result)

#Find the even number from the list using filter() function
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("Even number from list: ",result)

#Find the sum of all numbers in list using reduce() function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)
