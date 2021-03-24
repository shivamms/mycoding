# intevewing.io
# BFS Breadth First Search
# DFS depth first search
# Facebook Mock
# minimum number of steps
# shortest path problems
# recursive
# Write a function which accepts a positive integer and returns the minimum number of steps to get to 1 assuming we can perform the following operations:
# Subtract 1 from input
# Divide by 2 if the number is divisible by 2
# Divide by 3 if the number is divisible by 3

# taking advantage of the factor that we need only minumum number of node value in each leve to go to next level
# Non recursive
def minimumStepsToOne(num):
  if num == 1:
    return 0
  q = [(num,0)]
  steps = 0
  seen = set()

  while q:
    n, steps = q.pop() # knowing that the last inserted node is optimal one, we proceed from there
    if n == 1:
      return steps
    if n > 1 and n - 1 not in seen:
      seen.add(n-1)
      q.append((n-1,steps+1))
    if n % 2 == 0 and n // 2 >= 1 and n // 2 not in seen:
      seen.add(n // 2)
      q.append((n // 2,steps+1))
    if n % 3 == 0 and n // 3 >= 1 and n // 3 not in seen:
      seen.add(n // 3)
      q.append((n // 3, steps+1))
  return -1

# non recursive
# visit every node irrespective of if they are optimal node to proceed
def minimumStepsToOne(num):
  if num == 1:
    return 0
  q = [(num,0)]
  steps = 0
  seen = set()

  while q:
    n, steps = q.pop(0) # Not knowing that the last inserted node is optimal one, we visit every node
    if n == 1:
      return steps
    if n > 1 and n - 1 not in seen:
      seen.add(n-1)
      q.append((n-1,steps+1))
    if n % 2 == 0 and n // 2 >= 1 and n // 2 not in seen:
      seen.add(n // 2)
      q.append((n // 2,steps+1))
    if n % 3 == 0 and n // 3 >= 1 and n // 3 not in seen:
      seen.add(n // 3)
      q.append((n // 3, steps+1))
  return -1

#print(minimumStepsToOne(20))

# recursive solution BFS
# Breadth First Search
# taking advantage of the factor that we need only minumum number of node value in each level to go to next level
def minimumStepsToOneRecur(num):
  if num == 1:
    return 0
  
  def bfs(n,steps):
    q = []
    seen = set()
    if n == 1:
      return steps
    steps += 1
    if n > 1 and n - 1 not in seen:
      seen.add(n-1)
      q.append((n-1))
    if n % 2 == 0 and n // 2 >= 1 and n // 2 not in seen:
      seen.add(n // 2)
      q.append((n // 2))
    if n % 3 == 0 and n // 3 >= 1 and n // 3 not in seen:
      seen.add(n // 3)
      q.append((n // 3))
    return bfs(min(q),steps) # taking advantage of the fact that minimum value is the optimal node to proceed 
  return bfs(num, 0)
#print(minimumStepsToOneRecur(2))

# recursive solution DFS
# Depth First Search
# not taking advantage of the factor that we visit every node on each level
def dfs(num, steps):
  if num == 1:
    return steps
  a = b = c = float('inf')
  if num-1 >= 1:
    a = dfs(num-1, steps+1)
  if num%2 == 0 and num//2 > 1:
    b = dfs(num//2, steps+1)
  if num%3 == 0 and num//3 > 1:
    c = dfs(num//3, steps+1)
  return min(a,b,c)

print(dfs(20, 0))


