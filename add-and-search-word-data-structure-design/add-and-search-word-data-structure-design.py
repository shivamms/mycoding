class WordDictionary:

    def __init__(self):
        self.dictionary = dict()
        
    def addWord(self, word: str) -> None:
        curr = self.dictionary
        for letter in word:
            curr = curr.setdefault(letter, {})
        curr = curr.setdefault('__end__', '__end__')
            
    def search(self, word: str) -> bool:
        
        def searchWord(word, curr):
            for i, letter in enumerate(word):
                if letter not in curr:               
                    if letter == '.':
                        for x in curr:
                            if '__end__' != x and searchWord(word[i+1:], curr[x]):
                                return True
                    return False
                else:
                    curr = curr[letter]

            return '__end__' in curr
        
        curr = self.dictionary
        return searchWord(word, curr)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)