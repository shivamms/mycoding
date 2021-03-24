# interviewing.io
# finding distance between points
# use some kind of ordered dictionaries
# use some kind of heap queue
# facebook 
# heapq
# ordered kind of dictionaries
# list of tuples ordered
# need some good sorting algorithm for best time complexity
# Write an efficient program for printing the k closest points to a target point. Points have two dimensions: (x,y).

# For example, if you have the points [[1,1], [2,2], [3,3], ..., [10,10]] with a target of [5,5] and k = 3, you would print [[4,4], [5,5], [6,6]].

# Order of the output does not matter.

# The distance between two points (x0, y0) and (x1, y1) is the formula math.sqrt((x0-x1)**2 + (y0-y1)**2).
import math
import heapq

def closestPoints(pts,t,k):
  dists = []
  for p in(pts):
    heapq.heappush(dists, (math.sqrt((t[0]-p[0])**2 + (t[1]-p[1])**2),p))
  result = []
  for i in range(k):
    result.append(heapq.heappop(dists)[1])
  return result

pts = [[1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7],[8,8],[9,9], [10,10]]
t = [8,8]
k = 3
print(closestPoints(pts,t,k))