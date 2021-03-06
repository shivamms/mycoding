# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

def validPalindrome2(s):
    def ispalindrome(i, j):
      return all(s[k] == s[j - k + i] for k in range(i, j))

    for i in range(int(len(s) / 2)):
      if s[i] != s[~i]:
        j = len(s) - 1 - i
        return ispalindrome(i + 1, j) or ispalindrome(i, j - 1)
    return True


     
  