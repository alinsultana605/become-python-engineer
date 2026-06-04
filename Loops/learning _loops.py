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