#MUTABLE

#LIST
courses = ['Histroy', 'Math', 'Physics', 'CompSci']
courses_2 =['Art', 'Education']

print(courses) ## ['Histroy', 'Math', 'Physics', 'CompSci']
print(len(courses)) ## Number of element from the list, in this case is 4

#Access list
print(courses[0]) #Histroy
print(courses[3]) #CompSci
print(courses[-2]) #Physics
print(courses[0:2]) #['Histroy', 'Math']
print(courses[:2]) #['Histroy', 'Math']
print(courses[2:]) # ['Physics', 'CompSci']

#Add item in the list
courses.append('Art') # adding end of the list
print(courses) # ['Histroy', 'Math', 'Physics', 'CompSci', 'Art']
courses.insert(0,'Art') # Inserted at position
print(courses) # ['Art', 'Histroy', 'Math', 'Physics', 'CompSci', 'Art']


courses.extend(courses_2) # add the value from second list, difference between
                            # extend and append :
                            # ['Histroy', 'Math', 'Physics', 'CompSci', 'Art', 'Education'] ->extend
                            #['Histroy', 'Math', 'Physics', 'CompSci', ['Art', 'Education']]->append
print(courses) # ['Histroy', 'Math', 'Physics', 'CompSci', 'Art', 'Education']


courses.remove('Math') #['Histroy', 'Physics', 'CompSci', 'Art', 'Education']
                        # Remove specific element from the list
print(courses)

courses.pop()
print(courses) # ['Histroy', 'Physics', 'CompSci', 'Art']
                #Remove last element from the list

poped = courses.pop()
print(poped) # CompSci

courses.reverse()
print(courses) # ['CompSci', 'Physics', 'Math', 'Histroy']

courses.sort()
print(courses) #['CompSci', 'Histroy', 'Math', 'Physics'] alphabetical order

num = [1, 5, 4, 3, 2]
num.sort()
print(num) #[1, 2, 3, 4, 5] ascending sorting

num = [1, 5, 4, 3, 2]
num.sort(reverse=True)
print(num) #[5, 4, 3, 2, 1] descending sorting

##sorted function:
sorted_courses = sorted(courses)
print(sorted_courses) #['CompSci', 'Histroy', 'Math', 'Physics']


print(min(num)) #1
print(max(num)) #5
print(sum(num)) #15

print(courses.index('CompSci')) # 3 return index 

print('Art' in courses) #False
print('Math' in courses) # True

for item in courses:
    print(item) # print each item

for index, course in enumerate(courses):
    print(index, course)

#Return:
    """
0 Histroy
1 Math
2 Physics
3 CompSci
    """
    
for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = "- ".join(courses)
new_list = course_str.split("-")
print(course_str) #Histroy- Math- Physics- CompSci
print(new_list) # ['Histroy', ' Math', ' Physics', ' CompSci']