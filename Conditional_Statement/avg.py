marks1 = int(input("ENter 1st marks: "))
marks2 = int(input("ENter 2nd marks: "))
marks3 = int(input("ENter 3rd marks: "))

marks = [marks1, marks2, marks3]
marks.remove(min(marks))    # remove lowest mark

avg = sum(marks) / 2

print("The average marks of two subject is:" , avg)


''' another logic

total = m1 + m2 + m3
lowest = min(m1, m2, m3)

average = (total - lowest) / 2

'''