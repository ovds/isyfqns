def y(n,x):
    if n == 0:
        return 1
    else:
        return x**n + y(n - 1,x)

result = ""

with open('Question 2\input_question_2', 'r') as f:
    for line in f.readlines():
        input = line.split(' ')
        n = int(input[0])
        x = int(input[1])
        result += "{} {} {}\n".format(n,x,y(n,x))


f = open("Question 2\output_question_2.txt", "a")
f.write(result)
f.close()

