#Question 4: Basic

n = 1000

arr = []

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        arr.append(i)
        continue
    if i % 3 == 0:
        arr.append(i)
        continue
    if i % 5 == 0:
        arr.append(i)
        continue


f = open("output_question_4.txt", "a")
f.write(str(sum(arr)))
f.close()