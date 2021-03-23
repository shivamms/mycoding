## Time interval
# Facebook
# year intervals

#Problem: Given a group of people with their birth year and death year, find the year with highest population.

#Sample input
#[(2000,2010),(1975,2005),(1975,2003),(1803,1809),(1750,1869),(1842,1935),(1803,1921),(1894,1921)]

# Idea to solve this problem:
# Create a line chart for each element in this data set 
# for example:
#   b1--------------------d1
#      b2---------------------d2
#      b3----------d3
#              b4------------------d4
#                                      b5--------d5
# Now we need to find out the vertical line which passes through most 
# lines in the above chart

# Steps:
#1. Sort the list of tuples by asc birth year
#2. This forms a sorted interval
#3. Traverse throug the sets and narrow down the window between maximum birth year and minimum death year.
#4. If nobody born in any window (d4 and b5 in above example), then save the window discovered till now and start finding the new window.
#5. While doing so, count the persons in each window and save this information along with maximum deathyear of that window in a hash table
#6. Once all the tuples are traversed, find the maximum of number of persons from the hash table and find the year of that entry.

p = [(2000,2010),(1975,2005),(1975,2003),(1803,1809),(1750,1869),(1842,1935),(1803,1921),(1894,1921)]

def mostPopulatedYear(p):
  p = sorted(p, key = lambda x: x[0]) # O(n log n)
  # [(1750,1869),(1803,1921),(1803,1809),(1842,1935),(1894,1921),(1975,2003),(1975,2005),(2000,2010)]
  print(p)
  table = {} # space => w
  maxBirthYear = p[0][0] # 1750 space => 1
  minDeathYear = p[0][1] # 1869 space => 1
  count = 1
  n = len(p) # 8
  i = 0
  while i < n - 2: # O(n)
    if p[i][1] > p[i+1][0]: # 1869 > 1803
      maxBirthYear = p[i+1][0] # 1803
      if minDeathYear > p[i+1][1]: # 1869 > 1809
        minDeathYear = p[i+1][1] # 1809
      count += 1
    else:
      table[minDeathYear] = count
      count = 1
      maxBirthYear = p[i+1][0]
      minDeathYear = p[i+1][1]
    i += 1
  
  maxCount = max(list(table.values())) #O(n) space => 1
  for key, val in table.items(): # O(n) 
    if val == maxCount:
      return key

print(mostPopulatedYear(p))

# Time complexity => O(n log n + n + n + n) => O(nlogn)
# Space Complexity => w 