class Solution:
    def maxNumberOfBalloons(self,text: str) -> int:
        searchword = "balloon"
        searchcounts = Counter(searchword)
        textcounts = Counter(text)
        counts = []
        for key,val in searchcounts.items():
            if key in textcounts.keys():
                counts.append(textcounts[key] // searchcounts[key])
        if len(counts) == len(searchcounts):
            return min(counts)
        else:
            return 0
            