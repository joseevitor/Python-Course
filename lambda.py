students = [("Jose",23), ("Ana", 22), ("Lucas", 21)]
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)