import random

def gen_random_marks(num_students, min_mark, max_mark):
    marks = []
    for _ in range(num_students):
        mark = random.randint(min_mark, max_mark)
        marks.append(mark)
    return marks

num_students = 30  
min_mark = 0  
max_mark = 100  

random_marks =gen_random_marks(num_students, min_mark, max_mark)
print("Random marks:", random_marks)