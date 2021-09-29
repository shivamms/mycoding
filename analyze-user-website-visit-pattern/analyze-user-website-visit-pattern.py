class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:    
        def findPatterns(ws): 
            result = set()
            wlen = len(ws) 
            for i in range(wlen-2): 
                for j in range(i+1,wlen-1): 
                    for k in range(j+1, wlen): 
                        result.add((ws[i],ws[j],ws[k])) 
            return result

        usersites = defaultdict(list)
        patternscore = defaultdict(int)

        zipped = sorted(zip(timestamp,username,website), key=lambda tup: tup[0])

        for visit in zipped:
            usersites[visit[1]].append(visit[2])

        for key, value in usersites.items():
            visitedwebsites = len(value)
            if visitedwebsites == 3:
                patternscore[tuple(value)] += 1
            elif visitedwebsites > 3:
                patternlist = findPatterns(tuple(value))
                for p in patternlist:
                        patternscore[p] += 1

        highscore = 0
        result = []
        sortedbyvalue = sorted(patternscore.items(), key=lambda item: item[1],reverse=True)
        highscore = max(sortedbyvalue, key=lambda x: x[1])[1]
        highscorelist = [value for index, value in enumerate(sortedbyvalue) if value[1] == highscore]
        sortedbysites = sorted(highscorelist, key=lambda x: (x[0][0],x[0][1],x[0][2]))
        return list(sortedbysites[0][0])