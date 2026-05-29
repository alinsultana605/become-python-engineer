#Mutable
#Best performance 
cs_courses = {'Histroy', 'Math', 'Physics', 'CompSci'}
print(cs_courses) # {'Math', 'Physics', 'CompSci', 'Histroy'} aren t ordered
                    # if i run again this order can change each execution


cs_courses = {'Histroy', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)#{'CompSci', 'Histroy', 'Math', 'Physics'} remove duplicates

print('Math' in cs_courses) # True

## Intersection
art_courses = {'Histroy', 'Math', 'Design', 'Art'}
print(cs_courses.intersection(art_courses)) #{'Math', 'Histroy'}

#Union
print(cs_courses.union(art_courses)) #{'Art', 'Physics', 'CompSci', 'Math', 'Design', 'Histroy'}

#Empty list
empty_list = []
empty_list = list()

#Empty tuple
empty_tuple = ()
empty_tuple = tuple()

#Empty set
empty_set = {} #NOK it s dict
empty_set = set()

