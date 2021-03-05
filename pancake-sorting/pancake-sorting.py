# This problem does share some similarity with the Rubik's cube, i.e. one cannot move one tile without moving other tiles along with.
# Given the input of [3, 2, 4, 1], the desired sorted output would be [1, 2, 3, 4].
# the only operation that we could perform in order to move the elements in the list, is the so-called pancake flip, which is to reverse a prefix of the list.
# Starting from the largest value in the list, i.e. 4 in the example, its desired position would be the tail of the list. While in the input, it is located at the third of the list, if we look at the list from left to right.
# In order to move the value of 4 to its desired position, we could perform the following two steps:

# Firstly, we do the pancake flip on the prefix of [3, 2, 4]. With this operation, we then move the value 4 to the head of the updated list as [4, 2, 3, 1].
# flip to head

# Now that, the value 4 is located at the head of the list, we could now perform another pancake flip on the entire list, which would get us the list of [1, 3, 2, 4].
# flip to tail

# Voila. With the obtained list of [1, 3, 2, 4], we are now one step closer to our final goal, with the value 4 now at its proper place. For the following steps, we only need to focus on the sublist of [1, 3, 2].

# The idea is simple. First we move the number to the head of the list, then we can switch it with any other element by performing another pancake flip.

# The main algorithm runs a loop over the values of the list, starting from the largest one.

# At each round, we identify the value to sort (named as value_to_sort), which is the number we would put in place at this round.

# We then locate the index of the value_to_sort.

# If the value_to_sort is not at its place already, we can then perform at most two pancake flips as we explained in the intuition.

# At the end of the round, the value_to_sort would be put in place.

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        # start with largest number in the array as the first number to move
        # and move it to bottom
        numToMove = len(arr)
        while numToMove > 0:
            # identify the inde of the number to move
            index = arr.index(numToMove)
            # if it is not already in place
            if index != numToMove - 1:
                # flip the value to the head if necessary
                if index != 0:
                    arr = arr[:index+1][::-1] + arr[index+1:]
                    result.append(index+1)
                print(arr)
                arr = arr[:numToMove][::-1] + arr[numToMove:]
                print(arr)
                result.append(numToMove)
            numToMove -= 1
        return result
                
                