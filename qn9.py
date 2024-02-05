import matplotlib.path as mpltPath

points = []
polygon = []

with open("input_question_9_points.txt", "r") as f:
   points = [list(map(int, line.strip().split())) for line in f.readlines()]

with open("input_question_9_polygon.txt", "r") as f:
   polygon = [list(map(int, line.strip().split())) for line in f.readlines()]

def is_inside(polygon, point):
    n = len(polygon)
    inside = False
    x, y = point
    p1x,p1y = polygon[0]
    for i in range(n+1): #popular ray tracing method
        p2x,p2y = polygon[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

# Method 2: Using matplotlib library (much faster)
# path = mpltPath.Path(polygon)
# inside = path.contains_points(points)

f = open("output_question_9.txt", "a")
f.seek(0)
f.truncate()
for point in points:
    if is_inside(polygon, point):
        f.write(str(point[0]) + " " + str(point[1]) + " inside\n")
    else:
        f.write(str(point[0]) + " " + str(point[1]) + " outside\n")
f.close()