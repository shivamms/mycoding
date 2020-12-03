#Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.

#Use the Parameter Testing feature in the box below to test your code with different arguments.
def LongestWord(sen):

  # code goes here
  currentwordsize = 0
  largestwordsize = 0
  longestwordstart = 0
  largestword = []
  length = len(sen)
  for i in range(length):
    if (48 <= ord(sen[i]) <= 57) or (65 <= ord(sen[i]) <= 90) or (97 <= ord(sen[i]) <= 122):
        if currentwordsize == 0:
            longestwordstart = i
        currentwordsize += 1
    if (ord(sen[i]) == 32 or i == length - 1):
        if largestwordsize < currentwordsize:
            largestwordsize = currentwordsize
            largestword = sen[longestwordstart:longestwordstart + largestwordsize]
        currentwordsize = 0
  return largestword