Overview
Facebook interviewers like this question and propose it in four main variations. The choice of algorithm should be based on the input format:

Strings (the current problem). Use schoolbook digit-by-digit addition. Note, that to fit into constant space is not possible for languages with immutable strings, for example, for Java and Python. Here are two examples:

Add Binary: sum two binary strings.

Add Strings: sum two non-negative numbers in a string representation without converting them to integers directly.

Integers. Usually, the interviewer would ask you to implement a sum without using + and - operators. Use bit manipulation approach. Here is an example:

Sum of Two Integers: Sum two integers without using + and - operators.
Arrays. The same textbook addition. Here is an example:

Add to Array Form of Integer.
Linked Lists. Sentinel Head + Textbook Addition. Here are some examples:

Plus One.

Add Two Numbers.

Add Two Numbers II.



Approach 1: Elementary Math
Here we have two strings as input and asked not to convert them to integers. Digit-by-digit addition is the only option here.

Current
1 / 6
Algorithm

Initialize an empty res structure. Once could use array in Python and StringBuilder in Java.

Start from carry = 0.

Set a pointer at the end of each string: p1 = num1.length() - 1, p2 = num2.length() - 1.

Loop over the strings from the end to the beginning using p1 and p2. Stop when both strings are used entirely.

Set x1 to be equal to a digit from string nums1 at index p1. If p1 has reached the beginning of nums1, set x1 to 0.

Do the same for x2. Set x2 to be equal to digit from string nums2 at index p2. If p2 has reached the beginning of nums2, set x2 to 0.

Compute the current value: value = (x1 + x2 + carry) % 10, and update the carry: carry = (x1 + x2 + carry) / 10.

Append the current value to the result: res.append(value).

Now both strings are done. If the carry is still non-zero, update the result: res.append(carry).

Reverse the result, convert it to a string, and return that string.

