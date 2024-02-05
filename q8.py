from skimage import measure # an easy alternate way way to find the connected parts of an image
import numpy as np
import re

image = []

# read input_question_8.txt
with open("input_question_8.txt", "r") as f:
   for line in f.readlines():
      image.append(list(map(int, re.split(r'\D+', line.strip()))))

# Library method to find connected parts
# convert to numpy array
# image = np.array(image)
# connected_parts = measure.label(image, background=0)
# print(connected_parts)
      
# Custom method to find connected parts using 4-connectivity
def find_connected_parts(image):
   connected_parts = []
   rows = len(image)
   cols = len(image[0])
   visited = [[False for _ in range(cols)] for _ in range(rows)] #helps us in dfs

   def dfs(i, j, part): #recursive depth first search 
        if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or image[i][j] == 0: #if out of bounds or already visited or not a part of the connected part,
            return
        visited[i][j] = True #mark as visited
        part.append((i, j)) #add to the connected part
        #check the 8 directions
        dfs(i - 1, j, part) 
        dfs(i + 1, j, part)
        dfs(i, j - 1, part)
        dfs(i, j + 1, part)
        #uncomment or comment the following lines for 4-connectivity / 8-connectivity
        dfs(i - 1, j - 1, part)
        dfs(i - 1, j + 1, part)
        dfs(i + 1, j - 1, part)
        dfs(i + 1, j + 1, part)

   for i in range(rows):
      for j in range(cols):
         if not visited[i][j] and image[i][j] == 1:
            part = []
            dfs(i, j, part)
            connected_parts.append(part)

   return connected_parts

connected_parts = find_connected_parts(image)

connect_image = np.zeros((len(image), len(image[0])), dtype=int)
for i in range(len(connected_parts)):
   for j, k in connected_parts[i]:
      connect_image[j][k] = i + 1

np.savetxt('output_question_8.txt', connect_image, fmt='%d', delimiter=' ')



    
            


