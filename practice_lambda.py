#Find the cube of the number
from lamda_function import students

result = lambda x :x*x*x
print(result(5))

#check whether the number is positive or negative
num= lambda x : print("Positive") if x>0 else print("Negative")
num(-2)
num(3)

# OR
num= lambda x : "Positive" if x>0 else "Negative"
print(num(-2))
print(num(3))

#Use map() with lambda to double every number in a list
lis = [1,2,3,4,5]
result = list(map(lambda x : x*2,lis))
print(result)

#Use filter() with lambda to get all numbers greater than 10
lis = [10,20,8,9,20,30]
result = list(filter(lambda x : x>10 , lis))
print(result)

#Sort a list of tuples based on the second element using lambda function
students = [
    ("Sayali",22),
    ("Kunjan",13),
    ("Priyal",14)
]
result = sorted(students,key=lambda x:x[1])
print(result)