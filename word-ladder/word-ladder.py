class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        graph = defaultdict(list)
        wordLength = len(beginWord)
        for word in wordList:
            for i in range(wordLength):
                graph[word[:i] + '*' + word[i+1:]].append(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord}
        while queue:
            curWord, level = queue.popleft()
            if curWord == endWord:
                return level
            for i in range(wordLength):
                nextWord = curWord[:i] + '*' + curWord[i+1:]
                for word in graph[nextWord]:
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0