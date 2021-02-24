class Solution:
    def fullJustify(self,words: List[str], maxWidth: int) -> List[str]:
        wordListInALine = []
        lineLength = 0
        numberOfGapsInLIne = -1
        spaceBetweenWords = 0
        extraspaces = 0
        fullyJustified = []
        lastline = False
        for i in range(len(words)):
            if lineLength + numberOfGapsInLIne + len(words[i]) + 1 > maxWidth:
                if numberOfGapsInLIne <= 0:
                    spaceBetweenWords = maxWidth - lineLength
                    extraspaces = 0
                else:
                    spaceBetweenWords = (maxWidth - lineLength) // numberOfGapsInLIne
                    extraspaces = + (maxWidth - lineLength) % numberOfGapsInLIne
                fullyJustified.append(self.getLineSpaced(wordListInALine, spaceBetweenWords, extraspaces, lastline))
                wordListInALine = []
                lineLength = 0
                numberOfGapsInLIne = -1
                spaceBetweenWords = 0
                extraspaces = 0
            wordListInALine.append(words[i])
            lineLength += len(words[i])
            numberOfGapsInLIne += 1
        if len(wordListInALine) > 0:
            lastline = True
            spaceBetweenWords = maxWidth - lineLength
            extraspaces = 0
            fullyJustified.append(self.getLineSpaced(wordListInALine, spaceBetweenWords, extraspaces, lastline))
        return fullyJustified

    def getLineSpaced(self,wordlist, space, extraspaces, lastline):
        line = ""
        length = len(wordlist)
        if length == 1:
            line = wordlist[0] +  " " * space
            return line
        for i in range(length-1):
            if lastline:
                line += wordlist[i] + " "
            else:
                line += wordlist[i] + " " * space
                if extraspaces > 0:
                    line += " "
                    extraspaces -= 1
        line += wordlist[-1]
        if lastline:
            line += " " * (space - (length - 1))
        return line