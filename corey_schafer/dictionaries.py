# key : value pairs
student = {'name': 'Burak', 'age': 25, 'course': ['Math', 'CS']}
for k in student:
    print(f"{k}:{student.get(k)}")

print(student.keys())
print(student.values())
print(student.items())
