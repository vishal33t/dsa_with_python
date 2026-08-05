#sort()
arr = [5,1,4,2]
#  arr.sort()
#  print(arr)

#sorted
new_arr = sorted(arr)
#new_arr = sorted(arr,reverse=True)
print(new_arr)


#sorted String
names = ["Rahul","Amit","Vishal"]
print(sorted(names))

words = ["apple","hi","banana","cat"]
print(sorted(words,key=len))

students = [
    {"name":"Rahul","marks":80},
    {"name":"Aman","marks":95},
    {"name":"Vishal","marks":90}
]
students.sort(key=lambda x:x["marks"])
print(students)