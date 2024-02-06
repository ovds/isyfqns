import numpy as np

input_9 = [65, 72, 90, 110]
input_1000 = [2831, 4788, 5659, 6113]


# first method (by using minimum path and then "folding" the path to minus 1 every fold)
def find_path(m, n, s):
    path = np.concatenate((np.ones(m), np.arange(2, n+1)))
    remainder = s - np.sum(path)
    currSection = 1
    d = 0
    while remainder > 0:
        change = (m + n - 2) + currSection - n - d
        path[change] = currSection + 1  
        remainder -= 1
        d += 1
        if(d == n - 1):
            d = 0
            currSection += 1
        
    return path

# second method
def find_path2(m, n, s):
    path = np.zeros(m + n - 1)
    counter = 0
    s -= m * (m + 1) // 2
    if s < n - 1 or s > m * (n - 1):
        return None
    q = int(s / (n - 1))
    r = int(s % (n - 1))
    counter2 = 1
    while (counter < m + n - 1):
        if counter2 < q:
            path[counter]=counter2
            counter += 1
            counter2 += 1
            continue
        if counter2 > q:
            path[counter] = counter2
            counter += 1 
            counter2 += 1
            continue
        else :
            for i in range(0, n - r):
                path[counter] = counter2
                counter += 1
            counter2 += 1
            for i in range(0, r):
                path[counter] = counter2
                counter += 1
    return path

def convert_path_to_string(path):
    result = ""
    c = -1
    for i in path:
        if c == -1:
            c = i
        elif c == i:
            result += "R"
        else:
            result += "D"
            c = i
    return result

f = open("Question 7\output_question_7.txt", "a")

f.seek(0)
f.truncate()

for i in input_9:
    path = find_path2(9, 9, i)
    f.write(str(i) + " " + convert_path_to_string(path) + "\n")

f.write("\n")

for i in input_1000:
    path = find_path2(9, 1000, i)
    f.write(str(i) + " " + convert_path_to_string(path) + "\n")

f.close()






