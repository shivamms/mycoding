class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length+1)
        for i, r in enumerate(updates):
            arr[r[0]] = arr[r[0]] + r[2]
            arr[r[1]+1] = arr[r[1]+1] - r[2]
        for i in range(1,length):
            arr[i] = arr[i-1] + arr[i]
        return(arr[:length])