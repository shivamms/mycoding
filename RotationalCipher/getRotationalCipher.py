# Rotational Cipher
# One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
# Given a string and a rotation factor, return an encrypted string.
# Signature
# string rotationalCipher(string input, int rotationFactor)
# Input
# 1 <= |input| <= 1,000,000
# 0 <= rotationFactor <= 1,000,000
# Output
# Return the result of rotating input a number of times equal to rotationFactor.
# Example 1
# input = Zebra-493?
# rotationFactor = 3
# output = Cheud-726?
# Example 2
# input = abcdefghijklmNOPQRSTUVWXYZ0123456789
# rotationFactor = 39
# output = nopqrstuvwxyzABCDEFGHIJKLM9012345678



def getRotedChar(c,rf): 
  # add the rotation factor to ascii value
  rotated = ord(c) + rf
  # if character is lower case and rotated value is greater than the maximum value of ascii value for lower case character 
  if 97 <= ord(c) <= 122 and rotated > 122:
    # adjust the rotated value
      rotated = (rotated - 122) + 96
  # if character is upper case and rotated value is greater than the maximum value of ascii value for upper case character    
  elif 65 <= ord(c) <= 90 and rotated > 90:
    # adjust the rotated value
      rotated = (rotated - 90) + 64
  # if character is digit and rotated value is greater than the maximum value of ascii value for digit case character
  elif 48 <= ord(c) <= 57 and rotated > 57:
    # adjust the rotated value
      rotated = (rotated - 57) + 47
  return chr(rotated)
    

def rotationalCipher(input, rotation_factor):
  # do mod operation in case of rotation factior is greater than maximum number of charcter set
  # there will be two different set of rf
  rfa = rotation_factor % 26
  rfd = rotation_factor % 10
  # conver the input string to text
  text = list(input)
  for i , c in enumerate(text):
    if c.isdigit():
      text[i] = getRotedChar(c,rfd)
    elif c.isalpha():
      text[i] = getRotedChar(c,rfa)
  # join the list of characters
  return ''.join(text)

rotationalCipher('Zebra-493',3)

# Time complexity => O(n)
# Space Complexity => O(1)

