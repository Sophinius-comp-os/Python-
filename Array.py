
courses = ["Computer science", "Mobile App", "Data Science"]
print(courses)

print(courses[2]) # Accessing element in an array.


#Looping through an element
for y in courses:
    print("Course is", y)


#Adding a new element into an array
courses.append("Python")
print(courses)

#Deleting an element
courses.remove(courses[0])
print(courses)