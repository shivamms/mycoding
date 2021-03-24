# intevewing.io
# BFS Breadth First Search
# Facebook Mock
# minimum number of steps
# shortest path problems
# recursive
# Write a function which accepts a positive integer and returns the minimum number of steps to get to 1 assuming we can perform the following operations:
# Subtract 1 from input
# Divide by 2 if the number is divisible by 2
# Divide by 3 if the number is divisible by 3

def minimumStepsToOne(num):
  if num == 1:
    return 0
  q = [(num,0)]
  steps = 0
  seen = set()

  while q:
    n, steps = q.pop()
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

# recursive solution
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
    return bfs(min(q),steps)
  
  return bfs(num, 0)
print(minimumStepsToOneRecur(20))
