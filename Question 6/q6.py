import numpy as np

bits = ['1101100101', '1111011010', '1101101101', '1111011010', '1101100101', '1010010010', '1101101101', '1001011010', '0101100101', '1001010010']
arr = []

for bit in bits:
    same_count = 0
    for i in range(len(bit) - 1):
        if bit[i] == bit[i+1]:
            same_count += 1
    arr.append(same_count)

a = np.array(arr) #using numpy array for better performance since it has vectorized operations

#get frequency of each number
unique, counts = np.unique(a, return_counts=True) 
freq = np.asarray((unique, counts)).T #transpose to get the right format

np.savetxt('output_question_6.txt', freq, fmt='%d', delimiter=' ')