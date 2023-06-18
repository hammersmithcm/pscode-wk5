

numbers_str = input ("Enter your choice of numbers seperated by a space. Press enter when you are done: ")
numbers = [float (num) for num in numbers_str.split()]

total=0;
for x in numbers:
    total= total + x
print ("Average of ", numbers, "is", total/len(numbers))
print ("The maximum is", max(numbers))
print ("The minimum is", min(numbers))


