#for loops
nums = [1, 2, 3 ,4 ,5]

for num in nums:
    if num ==3:
        print("Found!")
        break # Broke the for loop
    print(num)



for num in nums:
    if num ==3:
        print("Found!")
        continue # skip tp the next iteration
    print(num)
"""
difference break and continue:
break : stop for now
continue: jump and go ahead
"""

for num in nums:
    for letter in "abc":
        print(num, letter)

for i in range(1, 10):
    print(i)

#while loopss

x = 0
while x < 10:
    if x ==5:
        break
    print(x)
    x+=1

#infinite loop
while True:
    print(x)
    x +=1

"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.


"""