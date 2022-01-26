class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        class Trie:
            def __init__(self):
                self.next = defaultdict(Trie)
                self.palindrome_suffix = []
                self.wordend = -1

        def makeTrie(words):
            root = Trie()
            for i, word in enumerate(words):
                word = word[::-1]
                curr = root
                for j, c in enumerate(word):
                    if word[j:] == word[j:][::-1]:
                        curr.palindrome_suffix.append(i)
                    curr = curr.next[c]
                curr.wordend = i
            return root

        trie = makeTrie(words)
        solutions = []
        for i, word in enumerate(words):
            curr = trie
            for j, c in enumerate(word):
                if curr.wordend != -1:
                    if word[j:] == word[j:][::-1]:
                        solutions.append([i, curr.wordend])
                if c not in curr.next:
                    break
                curr = curr.next[c]
            else:
                if curr.wordend != -1 and curr.wordend != i:
                    solutions.append([i, curr.wordend])
                for p in curr.palindrome_suffix:
                    solutions.append([i, p])
        return solutions